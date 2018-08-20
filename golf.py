#!/usr/bin/env python
# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'


import sys

import pygame
from pygame import draw

from transitions import Machine

from src import constants
from src.utils import colors


class Quit(Exception):
    pass


class GameOver(Exception):
    def __init__(self, surface):
        self.surface = surface


class Golf(object):
    STATES = [
        'home',
        'hole',
        'quit',
        'game_over',
    ]

    TRANSITIONS = [
        {'trigger': 'next_hole', 'source': ['home', 'hole'], 'dest': 'hole', 'before': 'load_hole'},
        {'trigger': 'end_game', 'source': 'hole', 'dest': 'game_over', 'before': 'render_final_score_text'},
        {'trigger': 'die', 'source': '*', 'dest': 'game_over', 'before': 'render_death_text'},
        {'trigger': 'quit', 'source': '*', 'dest': 'quit'},

    ]

    def __init__(self, screen, course):
        self.machine = Machine(
            model=self,
            initial='home',
            states=self.STATES,
            transitions=self.TRANSITIONS,
        )

        self.screen = screen

        self.clock = None

        self.course = course
        self.course.load()

        self.holes = course.holes
        self.iterable_holes = (hole for hole in self.holes)
        self.current_hole = None

        self.current_score = 0
        self.scores = []

    def home(self, clock):
        """
        Render text and wait for the user to press a key or click the mouse,
        at which point we start the game.
        """
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

        while True:
            for event in pygame.event.get():
                if event.type in [pygame.QUIT]:
                    self.quit()
                elif event.type in [pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN]:
                    self.next_hole()
                    return

            clock.tick(constants.MAX_FPS)

    def load_hole(self):
        """
        Advance to the next hole and reset the score.
        """
        self.current_hole = next(self.iterable_holes)
        self.current_hole.score = 0

    def handle_hole_tick(self):
        """
        Handle draw updates while playing an actual hole. Check for events,
        check for collisions, then update the game state and redraw the screen.
        """
        for event in pygame.event.get():
            self.current_hole.handle_event(event)

            if event.type in [pygame.QUIT]:
                self.quit()
            elif event.type in [pygame.USEREVENT]:
                if event.code == 'hole_complete':
                    try:
                        self.next_hole()
                    except StopIteration:
                        self.end_game()
                if event.code == 'die':
                    self.die(event.message)

        self.screen.fill(colors.DARKGRAY)
        self.current_hole.update()
        self.screen.blit(
            self.current_hole.draw(),
            (self.current_hole.origin.x, self.current_hole.origin.y)
        )

        self.screen.blit(
            self._draw_scores(30),
            (150, 900)
        )

        pygame.display.update()

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
        scores = [h.score for h in self.holes] + [self.course.total_score]

        for idx, par in enumerate(pars):
            par = str(par)
            score = str(scores[idx]) if scores[idx] != -1 else '-'

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

    def render_final_score_text(self):
        surface = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)

        font = pygame.font.Font(None, 50)
        par = "Par: {par}".format(par=self.course.total_par)
        score = "Score: {score}".format(score=self.course.total_score)

        width, height = font.size(score)
        surface.blit(
            font.render(score, True, colors.WHITE),
            (640 - (width // 2), 200)
        )

        width, _ = font.size(par)
        surface.blit(
            font.render(par, True, colors.WHITE),
            (640 - (width // 2), 215 + height)
        )

        raise GameOver(surface=surface)

    def render_death_text(self, msg):
        surface = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)

        font = pygame.font.Font(None, 50)

        width, height = font.size(msg)
        surface.blit(
            font.render(msg, True, colors.WHITE),
            (640 - (width // 2), 215 + height)
        )

        raise GameOver(surface=surface)

    def game_over(self, clock, surface=None):
        self.current_hole.update()
        self.current_hole.draw(show_pointer=False, show_velocity=False)

        self.screen.blit(
            self.current_hole.image,
            (self.current_hole.origin.x, self.current_hole.origin.y)
        )

        transparency = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        transparency.fill(colors.TRANSPARENTGRAY)
        self.screen.blit(
            transparency.convert_alpha(),
            (0, 0)
        )

        if isinstance(surface, pygame.Surface):
            self.screen.blit(
                surface.convert_alpha(),
                (0, 0)
            )

        font = pygame.font.Font(None, 30)
        width, _ = font.size('Press any key to quit...')
        self.screen.blit(
            font.render('Press any key to quit...', True, colors.WHITE),
            (640 - (width // 2), 850)
        )

        self.screen.blit(
            self._draw_scores(30),
            (150, 900)
        )

        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type in [pygame.QUIT, pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN]:
                    self.quit()
                    return 0

            clock.tick(constants.MAX_FPS)

    def handle_quit_tick(self):
        pygame.quit()
        raise Quit()

    def __call__(self):
        self.clock = pygame.time.Clock()

        self.home(self.clock)

        while True:
            state_handler = getattr(self, "handle_{self.state}_tick".format(self=self))

            try:
                state_handler()
            except (Quit, pygame.error):
                return 0
            except GameOver as go:
                return self.game_over(self.clock, go.surface)

            self.clock.tick(constants.MAX_FPS)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1280, 960))

    from courses.first_course import course as course1

    sys.exit(Golf(screen, course1)())
