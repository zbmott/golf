#!/usr/bin/env python
# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'


import sys

import pygame
from pygame import draw, math, mouse

from transitions import Machine

from src.utils import colors, Point


class Quit(Exception):
    pass


class Golf(object):
    STATES = [
        'home',
        'hole',
        'score',
        'quit',
    ]

    TRANSITIONS = [
        {'trigger': 'next_hole', 'source': ['home', 'hole'], 'dest': 'hole', 'before': 'load_hole'},
        {'trigger': 'end_game', 'source': 'hole', 'dest': 'score'},
        {'trigger': 'quit', 'source': '*', 'dest': 'quit'},
    ]

    def __init__(self, screen, course):
        self.machine = Machine(
            model=self,
            initial='home',
            states=self.STATES,
            transitions=self.TRANSITIONS
        )

        self.screen = screen

        self.clock = None

        self.course = course
        self.holes = course.holes
        self.iterable_holes = (hole for hole in self.holes)
        self.current_hole = None

        self.current_score = 0
        self.scores = []

    def handle_home_tick(self):
        """
        Describes how to draw the home screen. Basically all we do is render
        some text and wait for the user to press a key or click the mouse,
        at which point we start the game.
        """
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                self.quit()
            elif event.type in [pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN]:
                self.next_hole()

        screen.fill(colors.DARKGRAY)

        font1 = pygame.font.Font(None, 112)
        line1 = 'Golf'
        size1 = font1.size(line1)
        screen.blit(
            font1.render(line1, True, colors.WHITE),
            (640 - int(size1[0] / 2), 200)
        )

        font2 = pygame.font.Font(None, 46)
        line2 = 'Press any key to play...'
        size2 = font2.size(line2)
        screen.blit(
            font2.render(line2, True, colors.WHITE),
            (640 - int(size2[0] / 2), (200 + size1[1]) + 75)
        )

        pygame.display.update()

    def load_hole(self):
        """
        Record the current score, stop tracking the current hole's sprites,
        and advance to the next hole.
        """
        if self.current_hole is not None:
            self.scores.append(self.current_score)
            self.current_score = 0

            for group in self.current_hole.groups.values():
                group.empty()

        self.current_hole = next(self.iterable_holes)

    def handle_hole_tick(self):
        """
        Handle draw updates while playing an actual hole. Check for events,
        check for collisions, then update the game state and redraw the screen.
        """
        all = self.current_hole.groups['all']
        ball = self.current_hole.groups['ball'].sprites()[0]
        collidibles = self.current_hole.groups['collidibles']

        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                self.quit()
            elif event.type in [pygame.USEREVENT]:
                if event.code == 'hole_complete':
                    try:
                        self.next_hole()
                    except StopIteration:
                        self.end_game()
            elif event.type in [pygame.MOUSEBUTTONDOWN]:
                if event.button == 1:  # Left click
                    ball.strike(*event.pos)
                    self.current_score += 1

        collisions = ball.collide(collidibles)
        for collision in collisions:
            collision.handle_collision(ball)

        self.screen.fill(colors.DARKGRAY)
        all.update()
        dirty = all.draw(self.screen)

        self.screen.blit(
            self._draw_scores(30),
            (150, 900)
        )

        # Visualize the ball's current velocity
        if ball.velocity:
            self._visualize_vector(ball, self.screen)

        # Draw line from mouse pointer to ball
        if ball.velocity.length_squared() == 0:
            self._draw_pointer(ball, self.screen)

        pygame.display.update(dirty)

    def _draw_scores(self, size):
        """
        Draw the scorecard onto a new Surface and return it.
        """
        surface = pygame.Surface((1000, 2 * (size + 5)))
        surface.set_colorkey(colors.BLACK)

        font = pygame.font.Font(None, size)
        par_width, par_height = font.size('Par')

        draw.line(
            surface, colors.WHITE,
            (0, par_height + 3),
            (1000, par_height + 3),
            2
        )

        surface.blit(
            font.render('Par', True, colors.WHITE),
            (par_width // 2, 0)
        )

        surface.blit(
            font.render('Score', True, colors.WHITE),
            (3, par_height + 10)
        )

        pars = [h.par for h in self.holes] + [self.course.total_par]

        scores = self.scores + [self.current_score]
        scores += '-' * (len(pars) - len(scores) - 1)
        scores += [self.current_score + sum(self.scores)]

        for idx, par in enumerate(pars):
            par = str(par)
            score = str(scores[idx])

            x = (idx + 2) * par_width

            draw.line(surface, colors.WHITE, (x, 0), (x, 2 * (par_height + 5)), 2)

            width, _ = font.size(par)
            surface.blit(
                font.render(par, True, colors.WHITE),
                (x + ((par_width - width) // 2), 0)
            )

            width, _ = font.size(score)
            surface.blit(
                font.render(score, True, colors.WHITE),
                (x + ((par_width - width) // 2), par_height + 10)
            )

        return surface

    def _visualize_vector(self, ball, surface):
        """
        Draw a line that visualizes ball's current velocity.
        """
        draw.line(
            surface,
            (255, 0, 0),
            (ball.center.x, ball.center.y),
            (ball.center.x + int(ball.STRIKE_SCALE_FACTOR * ball.velocity.x),
             ball.center.y + int(ball.STRIKE_SCALE_FACTOR * ball.velocity.y)),
            3
        )

    def _draw_pointer(self, ball, surface):
        """
        Draw a line that visualizes strike direction and power.
        """
        mouse_pos = Point(*mouse.get_pos())
        mouse_vec = math.Vector2(
            mouse_pos.x - ball.center.x,
            mouse_pos.y - ball.center.y
        )

        if mouse_vec.length_squared() >= (ball.MAX_SPEED * ball.STRIKE_SCALE_FACTOR) ** 2:
            mouse_vec.scale_to_length(ball.MAX_SPEED * ball.STRIKE_SCALE_FACTOR)

        draw.line(
            surface,
            (0, 0, 255),
            (ball.center.x, ball.center.y),
            (int(ball.center.x - mouse_vec.x),
             int(ball.center.y - mouse_vec.y)),
            3
        )

    def handle_score_tick(self):
        """
        Draw the final score, then quit on user interaction.
        """
        for event in pygame.event.get():
            if event.type in [pygame.QUIT, pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN]:
                self.quit()

        screen.fill(colors.DARKGRAY)

        font = pygame.font.Font(None, 50)
        par = "Par: {par}".format(par=self.course.total_par)
        score = "Score: {score}".format(score=sum(self.scores))

        width, height = font.size(score)
        self.screen.blit(
            font.render(score, True, colors.WHITE),
            (640 - (width // 2), 200)
        )

        width, _ = font.size(par)
        self.screen.blit(
            font.render(par, True, colors.WHITE),
            (640 - (width // 2), 215 + height)
        )

        font = pygame.font.Font(None, 30)
        width, _ = font.size('Press any key to quit...')
        self.screen.blit(
            font.render('Press any key to quit...', True, colors.WHITE),
            (640 - (width // 2), 230 + 5*height)
        )

        self.screen.blit(
            self._draw_scores(30),
            (150, 900)
        )

        pygame.display.update()

    def handle_quit_tick(self):
        pygame.quit()
        raise Quit()

    def __call__(self):
        self.clock = pygame.time.Clock()

        while True:
            state_handler = getattr(self, "handle_{self.state}_tick".format(self=self))

            try:
                state_handler()
            except (Quit, pygame.error):
                return 0

            self.clock.tick(60)  # Framerate capped at 60 FPS


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1280, 960))

    from courses.first_course import course as course1

    sys.exit(Golf(screen, course1)())
