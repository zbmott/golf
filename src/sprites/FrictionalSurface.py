# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

from pygame import Rect, Surface
from pygame.sprite import DirtySprite

from src import constants
from .Collidible import Collidible


class FrictionalSurface(DirtySprite, Collidible):
    def __init__(self, point1, point2, color, friction, *groups):
        super().__init__(*groups)

        self._layer = constants.LAYER_GROUND

        self.width = abs(point2.x - point1.x)
        self.height = abs(point2.y - point1.y)
        self.color = color
        self.friction = friction

        self.image = Surface((
            self.width,
            self.height,
        ))

        self.rect = Rect(point1.x, point1.y, self.width, self.height)

        self.collision_rects = [self.rect]

    def update(self):
        self.image.fill(self.color, Rect(0, 0, self.width, self.height))

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
