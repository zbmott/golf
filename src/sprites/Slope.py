# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

import pygame

from src.utils import colors
from .abstract import Surface as SpriteSurface


class Slope(SpriteSurface):
    def __init__(self, points, color, vector, *groups):
        super().__init__(points, color, *groups)
        self.vector = vector

    def __repr__(self):
        points = ', '.join([repr(p) for p in self.points])
        return "Slope([{points}], Color{color!r}, Vector2({x}, {y}))".format(
            points=points,
            color=self.color,
            x=self.vector.x,
            y=self.vector.y,
        )

    @classmethod
    def create_for_editor(cls, points, *pos, **kw):
        return cls(points, colors.RED, pygame.math.Vector2(0, 0), *pos, **kw)

    def handle_collision(self, other):
        other.velocity += self.vector
