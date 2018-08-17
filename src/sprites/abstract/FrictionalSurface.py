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

    def handle_collision(self, ball):
        """
        Frictional surfaces scale the ball's velocity magnitude by a fixed
        coefficient (self.friction), and then stop the ball if the square
        of its velocity magnitude is less than constants.STOPPING_THRESHOLD.
        """
        try:
            ball.velocity.scale_to_length(
                ball.velocity.length() * self.friction
            )
        # ValueError will occur when ball.velocity.length() is 0;
        # i.e. when the ball is not moving.
        except ValueError:
            return

        if ball.velocity.length_squared() < constants.STOPPING_THRESHOLD:
            ball.stop()
