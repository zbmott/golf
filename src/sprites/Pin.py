# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'


from os import path

import pygame
from pygame import event, Rect

from src import constants
from src.utils import Point
from .Collidible import Collidible
from .ImageSprite import ImageSprite


class Pin(ImageSprite, Collidible):
    IMAGE_PATH = path.join(
        path.dirname(path.dirname(path.dirname(__file__))),
        'assets',
        'pin_25x25.png',
    )

    def __init__(self, point, *groups):
        super().__init__(*groups)

        self._layer = constants.LAYER_PIN

        self.rect.x = point.x
        self.rect.y = point.y

        self.collision_rects = [
            Rect(
                self.rect.x + (self.rect.width / 2),
                self.rect.y + (self.rect.height / 2),
                1,
                1
            )
        ]

    def __repr__(self):
        return "Pin({p!r})".format(p=Point(self.rect.x, self.rect.y))

    @property
    def center(self):
        return Point(self.collision_rects[0].x, self.collision_rects[0].y)

    def handle_collision(self, other):
        if other.velocity.length_squared() <= constants.SINK_THRESHOLD:
            other.stop()
            other.center_on(self.center)

            event.post(event.Event(pygame.USEREVENT, code='hole_complete'))
