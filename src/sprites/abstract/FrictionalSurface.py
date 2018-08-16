# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

from src import constants
from .Surface import Surface as SpriteSurface


class FrictionalSurface(SpriteSurface):
    def __init__(self, points, color, friction, *groups):
        super().__init__(points, color, *groups)
        self.friction = friction

    @classmethod
    def create_for_editor(cls, points, *pos, **kw):
        return cls(points, *pos, **kw)

    def handle_collision(self, other):
        try:
            other.velocity.scale_to_length(
                other.velocity.length() * self.friction
            )
        # ValueError will occur when other.velocity.length() is 0;
        # i.e. when the ball is not moving.
        except ValueError:
            return

        if other.velocity.length_squared() < constants.STOPPING_THRESHOLD:
            other.stop()
