# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'


from os import path

from pygame import Rect

from src.utils import Point
from .Collidible import Collidible
from .ImageSprite import ImageSprite


class Hole(ImageSprite, Collidible):
    IMAGE_PATH = path.join(
        path.dirname(path.dirname(path.dirname(__file__))),
        'assets',
        'hole_25x25.png',
    )
    SINK_THRESHOLD = 9

    def __init__(self, point, *groups):
        super().__init__(*groups)

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

    @property
    def center(self):
        return Point(self.collision_rects[0].x, self.collision_rects[0].y)

    def handle_collision(self, other):
        if other.velocity.length_squared() <= self.SINK_THRESHOLD:
            other.stop()
            other.center_on(self.center)
