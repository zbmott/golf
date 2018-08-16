#!/usr/bin/env python
# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

import copy, sys

from transitions import Machine

import pygame

from src.sprites import *
from src.sprites.abstract import FrictionalSurface
from src.utils import colors, Point, round_


class Quit(Exception):
    pass


class Editor(object):
    STATES = [
        'home',
        'placing',
    ]

    TRANSITIONS = [
        {'trigger': 'place', 'source': 'home', 'dest': 'placing'},
        {'trigger': 'finish', 'source': 'placing', 'dest': 'home', 'after': ['reset']},
        {'trigger': 'cancel', 'source': '*', 'dest': 'home', 'after': ['reset']}
    ]

    SPRITE_KEY_MAP = {
        (98, 0): GolfBall,  # B
        (103, 0): Green,    # G
        (108, 0): Slope,    # L
        (112, 0): Pin,      # P
        (114, 0): Rough,    # R
        (115, 0): Sand,     # S
        (119, 0): Wall      # W
    }

    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()

        self.machine = Machine(
            model=self,
            initial='home',
            states=self.STATES,
            transitions=self.TRANSITIONS,
        )

        self.all = pygame.sprite.LayeredUpdates()

        self.current_sprite_class = Green
        self.points = []

        self.canvas_origin = Point(50, 50)
        self.canvas = pygame.Surface((1080, 900))
        self.canvas_rect = pygame.Rect(50, 50, 1080, 900)

        self.orthogonal = False

    def _mouse_pos(self):
        """
        Return the current position of the mouse cursor relative to
        the canvas, snapped to a 10-pixel grid, and snapped to the
        x or y axis.
        """
        where = Point(*map(round_, pygame.mouse.get_pos())) - self.canvas_origin

        if self.should_snap_to_x(*where.as_2d_tuple()):
            where.y = self.points[-1].y
        elif self.should_snap_to_y(*where.as_2d_tuple()):
            where.x = self.points[-1].x

        return where

    def reset(self):
        self.points = []

    def should_snap_to_x(self, x, y):
        if not (self.points and self.orthogonal):
            return

        dx = abs(x - self.points[-1].x)
        dy = abs(y - self.points[-1].y)

        return dx > dy and dx - dy > 10

    def should_snap_to_y(self, x, y):
        if not (self.points and self.orthogonal):
            return

        dx = abs(x - self.points[-1].x)
        dy = abs(y - self.points[-1].y)

        return dy > dx and dy - dx > 10

    def tick(self):
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                raise Quit()
            if event.type in [pygame.MOUSEBUTTONDOWN]:
                if self.canvas_rect.collidepoint(*event.pos):
                    self.handle_click(event)
            if event.type in [pygame.KEYDOWN]:
                self.handle_keydown(event)
            if event.type in [pygame.KEYUP]:
                self.handle_keyup(event)

        self.screen.fill(colors.DARKGRAY)
        self.canvas.fill(colors.BLACK)

        self.all.update()
        self.all.draw(self.canvas)

        if self.state == 'placing':
            self.finalize(endpoint=self._mouse_pos(), save=False)

        self.screen.blit(
            self.canvas,
            self.canvas_origin.as_2d_tuple()
        )

        self.render_segment_length(self.screen, self.points)

        pygame.display.update()

    def render_segment_length(self, surface, points):
        p2 = self._mouse_pos()
        f = pygame.font.Font(None, 28)
        _, height = f.size('L =')

        surface.blit(
            f.render("{p.x}, {p.y}".format(p=p2), False, colors.WHITE),
            (10, 5)
        )

        if len(points) >= 1:
            dx = points[-1].x - p2.x
            dy = points[-1].y - p2.y

            d = (dx ** 2 + dy ** 2) ** 0.5

            surface.blit(
                f.render("L = {}".format(int(d)), False, colors.WHITE),
                (10, 10 + height)
            )

    def finalize(self, endpoint=None, save=False):
        points_to_draw = copy.copy(self.points)
        if endpoint:
            points_to_draw.append(endpoint)

        try:
            sprite = self.current_sprite_class.create_for_editor(points_to_draw)

        # Raised when we don't have enough points to draw a Wall (line).
        except IndexError:
            return

        # Raised when there aren't enough points to draw a Surface (polygon).
        except ValueError:
            return pygame.draw.aalines(
                self.canvas, colors.RED, False,
                [p.as_2d_tuple() for p in points_to_draw], 3
            )

        sprite.update()

        self.canvas.blit(
            sprite.image,
            (sprite.rect.x, sprite.rect.y)
        )

        if save:
            self.all.add(sprite)

    def handle_click(self, event):
        button = event.button
        where = self._mouse_pos()

        if button != 1:
            return

        if self.state == 'home':
            self.place()

        if self.state == 'placing':
            self.points.append(where)

            # Convenience logic for non-polygonal objects
            if len(self.points) == 2:
                self.finalize(save=True)

                # If we're placing a 0-D object, finish placement after the 2nd click.
                if issubclass(self.current_sprite_class, (GolfBall, Pin)):
                    self.finish()

                # If we're placing a 1-D object, finish placement, but start placing
                # another object where the first one left off.
                elif issubclass(self.current_sprite_class, (Wall,)):
                    self.points = self.points[1:]

    def handle_keydown(self, event):
        print("KEYDOWN: {event.key}, {event.mod}".format(event=event))

        if event.key == 115 and event.mod == 1024:  # Cmd/Ctrl + S
            self.save()

        if self.state == 'placing' and event.key == 32:  # Spacebar
            self.finalize(save=True)
            self.finish()

        if event.key in {303, 304}:  # Shift
            self.orthogonal = True

        if (event.key, event.mod) in self.SPRITE_KEY_MAP:
            self.current_sprite_class = self.SPRITE_KEY_MAP[(event.key, event.mod)]

        if event.key == 27:  # Esc
            self.cancel()

    def handle_keyup(self, event):
        if event.key in {303, 304}:
            self.orthogonal = False

    def save(self):
        tmpl = """
from pygame import Color, font
from pygame.math import Vector2
from pygame.sprite import LayeredDirty

from src.models import Hole as BaseHole
from src.sprites import *
from src.utils import colors, Point


Hole = BaseHole(
    'untitled',
    par=3,
    origin={origin!r},
    ball={ball_pos!r},
    noncollidibles=LayeredDirty(),
    collidibles=LayeredDirty(
        {collidibles}
    )
)
"""
        ball = None
        for s in self.all.sprites():
            if isinstance(s, GolfBall):
                ball = s
                break

        self.all.remove(ball)

        with open('new_hole.py', 'w') as outfile:
            outfile.write(
                tmpl.format(
                    origin=self.canvas_origin,
                    ball_pos=Point(
                        int(ball.logical_position.x),
                        int(ball.logical_position.y),
                    ),
                    collidibles=(",\n" + 8*' ').join([repr(s) for s in self.all.sprites()])
                )
            )

        pygame.quit()
        raise Quit()

    def __call__(self):
        while True:
            try:
                self.tick()
            except Quit:
                return 0

            self.clock.tick(60)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1180, 1000))

    sys.exit(Editor(screen)())
