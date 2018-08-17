# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

from pygame import draw, mask, Rect, sprite, Surface as PyGameSurface

from src import constants
from src.utils import colors, Point
from .Collidible import Collidible


class Surface(sprite.DirtySprite, Collidible):
    def __init__(self, points, color, *groups):
        super().__init__(*groups)

        self._layer = constants.LAYER_GROUND

        self.points = points
        self.origin = Point(
            min([p.x for p in points]),
            min([p.y for p in points])
        )

        self.width = max([p.x for p in points]) - self.origin.x
        self.height = max([p.y for p in points]) - self.origin.y
        self.color = color

        self.image = PyGameSurface((
            self.width,
            self.height,
        ))
        self.image.set_colorkey(colors.BLACK)

        self.rect = Rect(self.origin.x, self.origin.y, self.width, self.height)

        self.update()

        # Make sure we don't try to make a mask from a 1-D image.
        if self.width * self.height == 0:
            raise ValueError()

        self.mask = mask.from_surface(self.image)

    def __repr__(self):
        return "{cls}([{points}])".format(
            cls=self.__class__.__name__,
            points=', '.join([repr(p) for p in self.points])
        )

    @classmethod
    def create_for_editor(cls, points):
        return cls(points)

    def collide_with(self, ball):
        """
        Surfaces only collide with the ball if the ball is currently moving.
        """
        if ball.should_collide_with_surface:
            super().collide_with(ball)

    def update(self):
        draw.polygon(
            self.image,
            self.color,
            [(p.x - self.origin.x, p.y - self.origin.y) for p in self.points],
        )

    def handle_collision(self, other):
        raise NotImplementedError()
