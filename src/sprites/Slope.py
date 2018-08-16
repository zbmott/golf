# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

from pygame import Rect

from src.utils import Point
from .abstract import Surface as SpriteSurface


class Slope(SpriteSurface):
    def __init__(self, point1, point2, color, vector, *groups):
        super().__init__(point1, point2, color, *groups)
        self.vector = vector

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
