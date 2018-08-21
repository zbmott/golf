# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

from os import path

from pygame import math

from .Pin import Pin


class Tunnel(Pin):
    IMAGE_PATH = path.join(
        path.dirname(path.dirname(path.dirname(__file__))),
        'assets',
        'tunnel_25x25.png',
    )

    def __init__(self, point, exit, vector, *groups):
        super().__init__(point, *groups)
        self.exit = exit
        self.vector = vector

    def __repr__(self):
        return "Tunnel({p1!r}, {p2!r}, Vector2({x}, {y}))".format(
            p1=self.points[0],
            p2=self.exit,
            x=self.vector.x,
            y=self.vector.y
        )

    @classmethod
    def create_for_editor(cls, points):
        if len(points) < 3:
            return cls(points[-1], None, math.Vector2(0, 0))

        return cls(points[-2], points[-1], math.Vector2(0, 0))

    @classmethod
    def should_finalize(cls, points):
        return len(points) == 3

    def sink_putt(self, ball):
        ball.center_on(self.exit)
        ball.velocity = self.vector
