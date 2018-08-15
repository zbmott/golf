# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

import pickle, sys

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
        self.start_point = None
        self.end_point = None

        self.canvas_origin = Point(50, 50)
        self.canvas = pygame.Surface((1080, 900))
        self.canvas_rect = pygame.Rect(50, 50, 1080, 900)

        self.orthogonal = False

    def reset(self):
        self.start_point = None
        self.end_point = None

    def should_snap_to_x(self, x, y):
        if not (self.start_point and self.orthogonal):
            return

        dx = abs(x - self.start_point.x)
        dy = abs(y - self.start_point.y)

        return dx > dy and dx - dy > 10

    def should_snap_to_y(self, x, y):
        if not (self.start_point and self.orthogonal):
            return

        dx = abs(x - self.start_point.x)
        dy = abs(y - self.start_point.y)

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
                print("KEYDOWN: {event.key}, {event.mod}".format(event=event))

                if event.key == 115 and event.mod == 1024:  # Cmd/Ctrl + S
                    self.save()

                if event.key in {303, 304}:  # Shift
                    self.orthogonal = not self.orthogonal

                if (event.key, event.mod) in self.SPRITE_KEY_MAP:
                    self.current_sprite_class = self.SPRITE_KEY_MAP[(event.key, event.mod)]

                if event.key == 27:  # Esc
                    self.cancel()

        self.screen.fill(colors.DARKGRAY)
        self.canvas.fill(colors.BLACK)

        self.all.update()
        self.all.draw(self.canvas)

        if self.state == 'placing':
            self.finalize(False)

        self.screen.blit(
            self.canvas,
            self.canvas_origin.as_2d_tuple()
        )

        pygame.display.update()

    def finalize(self, save=False):
        x, y = pygame.mouse.get_pos()
        end_point = Point(
            round_(x - self.canvas_origin.x),
            round_(y - self.canvas_origin.y)
        )

        if self.start_point == end_point:
            return

        def _normalize_coords(start, end):
            minx = min(start.x, end.x)
            miny = min(start.y, end.y)
            maxx = max(start.x, end.x)
            maxy = max(start.y, end.y)

            return Point(minx, miny), Point(maxx, maxy)

        if issubclass(self.current_sprite_class, FrictionalSurface):
            sprite = self.current_sprite_class(
                *_normalize_coords(self.start_point, end_point)
            )

        elif issubclass(self.current_sprite_class, Slope):
            sprite = self.current_sprite_class(
                *_normalize_coords(self.start_point, end_point),
                colors.RED,
                pygame.math.Vector2(0, 1),
        )

        elif issubclass(self.current_sprite_class, Wall):
            if self.should_snap_to_x(*end_point.as_2d_tuple()):
                end_point.y = self.start_point.y
            elif self.should_snap_to_y(*end_point.as_2d_tuple()):
                end_point.x = self.start_point.x

            sprite = self.current_sprite_class(self.start_point, end_point)

        elif issubclass(self.current_sprite_class, (GolfBall, Pin)):
            sprite = self.current_sprite_class(end_point)

        sprite.update()

        self.canvas.blit(
            sprite.image,
            (sprite.rect.x, sprite.rect.y)
        )

        if save:
            self.all.add(sprite)

    def handle_click(self, event):
        button = event.button
        where = Point(
            round_(event.pos[0] - self.canvas_origin.x),
            round_(event.pos[1] - self.canvas_origin.y)
        )

        if button != 1:
            return

        if self.state == 'home':
            self.start_point = where
            self.place()
        elif self.state == 'placing':
            self.finalize(save=True)
            self.finish()

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
