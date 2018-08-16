# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

from pygame import mask, Rect, Surface
from pygame.sprite import DirtySprite

from src import constants
from src.utils import colors, Point
from .Collidible import Collidible


class Slope(DirtySprite, Collidible):
    def __init__(self, point1, point2, color, vector, *groups):
        super().__init__(*groups)

        self._layer = constants.LAYER_GROUND

        self.width = abs(point2.x - point1.x)
        self.height = abs(point2.y - point1.y)
        self.color = color
        self.vector = vector

        self.image = Surface((
            self.width, self.height
        ))
        self.image.set_colorkey(colors.BLACK)

        self.rect = Rect(point1.x, point1.y, self.width, self.height)

        self.update()
        self.mask = mask.from_surface(self.image)

    def __repr__(self):
        p1 = Point(self.rect.x, self.rect.y)
        p2 = Point(self.rect.x + self.rect.width, self.rect.y + self.rect.height)
        return "Slope({p1!r}, {p2!r}, Color{color!r}, Vector2({x}, {y}))".format(
            p1=p1,
            p2=p2,
            color=self.color,
            x=self.vector.x,
            y=self.vector.y,
        )

    def update(self):
        self.image.fill(self.color, Rect(0, 0, self.width, self.height))

    def handle_collision(self, other):
        other.velocity += self.vector
