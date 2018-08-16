# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

from pygame import mask, Rect, sprite, Surface as PyGameSurface

from src import constants
from src.utils import colors
from .Collidible import Collidible


class Surface(sprite.DirtySprite, Collidible):
    def __init__(self, point1, point2, color, *groups):
        super().__init__(*groups)

        self._layer = constants.LAYER_GROUND

        self.width = abs(point2.x - point1.x)
        self.height = abs(point2.y - point1.y)
        self.color = color

        if self.width * self.height == 0:
            raise ValueError('Surface cannot be 1-dimensional')

        self.image = PyGameSurface((
            self.width,
            self.height,
        ))
        self.image.set_colorkey(colors.BLACK)

        self.rect = Rect(point1.x, point1.y, self.width, self.height)

        self.update()
        self.mask = mask.from_surface(self.image)

    def update(self):
        raise NotImplementedError()

    def handle_collision(self, other):
        raise NotImplementedError()
