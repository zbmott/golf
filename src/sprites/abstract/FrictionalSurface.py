# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'


from pygame import draw, Rect

from src import constants
from .Surface import Surface as SpriteSurface


class FrictionalSurface(SpriteSurface):
    def __init__(self, point1, point2, color, friction, *groups):
        super().__init__(point1, point2, color, *groups)
        self.friction = friction

    def update(self):
        draw.rect(
            self.image,
            self.color,
            Rect(0, 0, self.width, self.height)
        )

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
