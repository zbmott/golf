#!/usr/bin/env python
# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'


import sys

import pygame
from pygame import draw, math, mouse

from transitions import Machine

from src.utils import Point


class Golf(object):
    STATES = [
        'home',
        'hole',
        'score',
    ]

    TRANSITIONS = [
        {'trigger': 'start_game', 'source': 'home', 'dest': 'hole'},
        {'trigger': 'next_hole', 'source': 'hole', 'dest': 'hole', 'before': 'load_hole'},
        {'trigger': 'end_game', 'source': 'hole', 'dest': 'score'},
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
        self.hole = next(course)

    def handle_home_tick(self):
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
            elif event.type in [pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN]:
                self.start_game()

        screen.fill((50, 50, 50))

        font1 = pygame.font.Font(None, 112)
        line1 = 'Golf'
        size1 = font1.size(line1)
        screen.blit(
            font1.render(line1, True, (235, 235, 235)),
            (640 - int(size1[0] / 2), 200)
        )

        font2 = pygame.font.Font(None, 46)
        line2 = 'Press any key to play...'
        size2 = font2.size(line2)
        screen.blit(
            font2.render(line2, True, (235, 235, 235)),
            (640 - int(size2[0] / 2), (200 + size1[1]) + 75)
        )

        pygame.display.update()

    def load_hole(self):
        self.hole = next(self.course)

    def handle_hole_tick(self):
        keystate = None

        all = self.hole.groups['all']
        ball = self.hole.groups['ball'].sprites()[0]
        collidibles = self.hole.groups['collidibles']

        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
            elif event.type in [pygame.USEREVENT]:
                if event.code == 'hole_complete':
                    try:
                        self.next_hole()
                    except StopIteration:
                        self.end_game()
            elif event.type in [pygame.VIDEORESIZE]:
                self.screen = pygame.display.set_mode(event.size)
            elif event.type in [pygame.MOUSEBUTTONDOWN]:
                if event.button == 1:  # Left click
                    ball.strike(*event.pos)
            elif event.type in [pygame.KEYDOWN]:
                keystate = event.key

        if keystate == 115:  # 's'
            ball.stop()

        collisions = ball.collide(collidibles)
        for collision in collisions:
            collision.handle_collision(ball)

        self.screen.fill((50, 50, 50))
        all.update()
        dirty = all.draw(self.screen)

        # Visualize the ball's current velocity
        if ball.velocity:
            draw.line(
                self.screen,
                (255, 0, 0),
                (ball.center.x, ball.center.y),
                (ball.center.x + int(ball.STRIKE_SCALE_FACTOR*ball.velocity.x),
                 ball.center.y + int(ball.STRIKE_SCALE_FACTOR*ball.velocity.y)),
                3
            )

        # Draw line from mouse pointer to ball
        if ball.velocity.length_squared() == 0:
            mouse_pos = Point(*mouse.get_pos())
            mouse_vec = math.Vector2(
                mouse_pos.x - ball.center.x,
                mouse_pos.y - ball.center.y
            )

            if mouse_vec.length_squared() >= (ball.MAX_SPEED*ball.STRIKE_SCALE_FACTOR)**2:
                mouse_vec.scale_to_length(ball.MAX_SPEED * ball.STRIKE_SCALE_FACTOR)

            draw.line(
                self.screen,
                (0, 0, 255),
                (ball.center.x, ball.center.y),
                (int(ball.center.x - mouse_vec.x),
                 int(ball.center.y - mouse_vec.y)),
                3
            )

        pygame.display.update(dirty)

    def handle_score_tick(self):
        pygame.quit()

    def __call__(self):
        self.clock = pygame.time.Clock()

        while True:
            state_handler = getattr(self, "handle_{self.state}_tick".format(self=self))

            try:
                state_handler()
            except pygame.error:
                return 0

            self.clock.tick(60)  # Framerate capped at 60 FPS


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1280, 960))

    from courses.first_course import course as course1

    sys.exit(Golf(screen, course1)())
