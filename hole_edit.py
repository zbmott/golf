#!/usr/bin/env python
# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

import importlib, copy, sys
from operator import attrgetter

from transitions import Machine

import pygame

from src.models import Hole
from src.sprites import *
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
        (110, 0): Tunnel,   # N
        (112, 0): Pin,      # P
        (114, 0): Rough,    # R
        (115, 0): Sand,     # S
        (116, 0): Water,    # T
        (118, 0): Lava,     # V
        (119, 0): Wall      # W
    }

    def __init__(self, screen, hole=None):
        self.screen = screen
        self.clock = pygame.time.Clock()

        self.machine = Machine(
            model=self,
            initial='home',
            states=self.STATES,
            transitions=self.TRANSITIONS,
        )

        self.hole = hole or Hole()

        self.hole.groups['all'].add(hole.ball)

        self.current_sprite_class = None if self.hole else Green

        self.points = []

        self.orthogonal = False
        self.selection = None

    def _mouse_pos(self):
        """
        Return the current position of the mouse cursor relative to
        the canvas, snapped to a 10-pixel grid, and snapped to the
        x or y axis.
        """
        where = Point(*map(round_, pygame.mouse.get_pos())) - self.hole.origin

        if self.should_snap_to_x(*where.as_2d_tuple()):
            where.y = self.points[-1].y
        elif self.should_snap_to_y(*where.as_2d_tuple()):
            where.x = self.points[-1].x

        return where

    def reset(self):
        self.current_sprite_class = None
        self.selection = None
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
                if self.hole.rect.collidepoint(*event.pos):
                    self.handle_click(event)
            if event.type in [pygame.KEYDOWN]:
                self.handle_keydown(event)
            if event.type in [pygame.KEYUP]:
                self.handle_keyup(event)

        self.screen.fill(colors.DARKGRAY)
        self.hole.image.fill(colors.BLACK)

        self.hole.groups['all'].update()
        self.hole.draw(show_pointer=False, show_velocity=False)

        if self.state == 'placing':
            self.finalize(endpoint=self._mouse_pos(), save=False)

        self.screen.blit(
            self.hole.image,
            self.hole.origin.as_2d_tuple()
        )

        self.render_segment_length(self.screen, self.points)
        self.render_selection(self.screen)

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

    def render_selection(self, surface):
        if self.selection is None:
            return

        target = self.selection.rect

        pygame.draw.rect(surface, colors.WHITE, pygame.Rect(  # Upper left
            self.hole.origin.x + target.x - 3,
            self.hole.origin.y + target.y - 3,
            3, 3
        ))
        pygame.draw.rect(surface, colors.WHITE, pygame.Rect(  # Upper right
            self.hole.origin.x + target.x + target.width,
            self.hole.origin.y + target.y - 3,
            3, 3
        ))
        pygame.draw.rect(surface, colors.WHITE, pygame.Rect(  # Bottom left
            self.hole.origin.x + target.x - 3,
            self.hole.origin.y + target.y + target.height,
            3, 3
        ))
        pygame.draw.rect(surface, colors.WHITE, pygame.Rect(  # Bottom right
            self.hole.origin.x + target.x + target.width,
            self.hole.origin.y + target.y + target.height,
            3, 3
        ))

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
                self.hole.image, colors.RED, False,
                [p.as_2d_tuple() for p in points_to_draw], 3
            )

        sprite.update()

        self.hole.image.blit(
            sprite.image,
            (sprite.rect.x, sprite.rect.y)
        )

        if save:
            self.hole.groups['all'].add(sprite)
            self.hole.groups['collidibles'].add(sprite)

    def handle_click(self, event):
        button = event.button
        where = self._mouse_pos()

        if button != 1:
            return

        if self.state == 'home':
            self.selection = None
            if self.current_sprite_class is not None:
                self.place()
            else:
                self.selection = self.select(where)

        if self.current_sprite_class is not None:
            self.points.append(where)

            if self.current_sprite_class.should_finalize(self.points):
                self.finalize(save=True)

                # Convenience logic for special cases.
                # If we're placing a 0-D object, finish placement after the 2nd click.
                if issubclass(self.current_sprite_class, (GolfBall, Pin, Tunnel)):
                    self.finish()

                # If we're placing a 1-D object, finish placement, but start placing
                # another object where the first one left off.
                elif issubclass(self.current_sprite_class, (Wall,)):
                    self.points = self.points[1:]

    def select(self, pos):
        """
        Return the topmost sprite whose rect contains the given position.
        This could be improved by making a 1x1 mask at that location and
        using sprite.collide_mask instead of rect.collidepoint.
        """
        for s in sorted(self.hole.groups['all'].sprites(), key=attrgetter('_layer'), reverse=True):
            if s.rect.collidepoint(pos.as_2d_tuple()):
                return s

        return None

    def handle_keydown(self, event):
        print("KEYDOWN: {event.key}, {event.mod}".format(event=event))

        if event.key == 115 and event.mod > 0:  # Cmd/Ctrl + S
            self.save()

        if self.state == 'placing' and event.key == 32:  # Spacebar
            self.finalize(save=True)
            self.finish()

        if event.key in {303, 304}:  # Shift
            self.orthogonal = True

        if (event.key, event.mod) in self.SPRITE_KEY_MAP:
            self.current_sprite_class = self.SPRITE_KEY_MAP[(event.key, event.mod)]
            if self.selection is not None:
                self._replace_selection()

        if event.key == 27:  # Esc
            self.cancel()

        if event.key in {8, 127}:  # Backspace, Delete:
            if self.selection:
                self.selection.kill()
                self.selection = None

    def handle_keyup(self, event):
        if event.key in {303, 304}:
            self.orthogonal = False

    def _replace_selection(self):
        """
        Replace self.selection with an instance of self.current_sprite_class.
        """
        try:
            new = self.current_sprite_class.create_for_editor(self.selection.points)
        except (ValueError, TypeError, IndexError):
            pass
        else:
            self.hole.groups['all'].add(new)
            self.hole.groups['collidibles'].add(new)
            self.selection.kill()
            self.selection = new

    def save(self):
        tmpl = """
from pygame import Color, font
from pygame.math import Vector2
from pygame.sprite import LayeredDirty

from src.models import Hole as BaseHole
from src.sprites import *
from src.utils import colors, Point


Hole = BaseHole(
    {hole.name!r},
    par={hole.par},
    origin={origin!r},
    ball={ball_pos!r},
    noncollidibles=LayeredDirty(),
    collidibles=LayeredDirty(
        {collidibles}
    )
)
"""
        ball = None
        for s in self.hole.groups['all'].sprites():
            if isinstance(s, GolfBall):
                ball = s
                break

        self.hole.groups['all'].remove(ball)

        with open('new_hole.py', 'w') as outfile:
            outfile.write(
                tmpl.format(
                    hole=self.hole,
                    origin=self.hole.origin,
                    ball_pos=Point(
                        int(ball.logical_position.x),
                        int(ball.logical_position.y),
                    ),
                    collidibles=(",\n" + 8*' ').join([
                        repr(s)
                        for s in self.hole.groups['collidibles'].sprites()
                    ])
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

    try:
        hole = importlib.import_module(sys.argv[1]).Hole
    except ImportError:
        hole = None

    sys.exit(Editor(screen, hole=hole)())
