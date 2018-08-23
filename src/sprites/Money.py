# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'


from os import path

from src import constants
from .abstract import Collidible, ImageSprite


class Money(ImageSprite, Collidible):
    IMAGE_PATH = path.join(
        path.dirname(path.dirname(path.dirname(__file__))),
        'assets',
        'coin_15x15.png',
    )

    def __init__(self, point, amount=1, *groups):
        super().__init__()

        self.point = point
        self.amount = amount
        self._layer = constants.LAYER_WALL
        self.add(*groups)

        self.rect.x = point.x
        self.rect.y = point.y

    def __repr__(self):
        return "{self.__class__.__name__}({self.point!r}, amount={self.amount!r})".format(self=self)

    @classmethod
    def create_for_editor(cls, points):
        return cls(points[-1])

    @classmethod
    def should_finalize(cls, points):
        return len(points) == 2

    def handle_collision(self, ball):
        ball.funds += self.amount
        self.kill()
