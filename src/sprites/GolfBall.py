# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

from os import path

from pygame import math, Rect

from src import constants
from src.utils import Point
from .abstract import ImageSprite


class GolfBall(ImageSprite):
    RADIUS = 10
    IMAGE_PATH = path.join(
        path.dirname(path.dirname(path.dirname(__file__))),
        'assets',
        'golfball_20x20.png'
    )
    STRIKE_SCALE_FACTOR = 7.5

    def __init__(self, point, *groups):
        super().__init__(*groups)

        self._layer = constants.LAYER_BALL

        self.velocity = math.Vector2(0, 0)

        self.logical_position = Point(point.x - self.RADIUS, point.y - self.RADIUS)

        self.rect.x = self.logical_position.x
        self.rect.y = self.logical_position.y

        self.previous_positions = []
        self.previous_velocities = []

    @property
    def center(self):
        return Point(
            int(self.logical_position.x + self.RADIUS),
            int(self.logical_position.y + self.RADIUS)
        )

    @property
    def collision_rect(self):
        return Rect(
            self.rect.x + 2, self.rect.y + 2,
            self.rect.width - 4, self.rect.height - 4
        )

    @property
    def should_collide_with_surface(self):
        """
        The ball shouldn't collide with a surface if it isn't moving.
        (I.e. x and y velocity components are 0.)
        """
        return abs(self.velocity.x) > 0 or abs(self.velocity.y) > 0

    @classmethod
    def create_for_editor(cls, points):
        return cls(points[-1])

    def update(self):
        self.logical_position.x += self.velocity.x
        self.logical_position.y += self.velocity.y

        # Update the ball's physical position to match the pixels
        # nearest its logical position.
        self.rect.x = int(self.logical_position.x)
        self.rect.y = int(self.logical_position.y)

        self.dirty = 1

    def set_logical_pos(self, point):
        self.logical_position = point

    def center_on(self, point):
        self.set_logical_pos(Point(point.x - self.RADIUS, point.y - self.RADIUS))

    def strike(self, x, y):
        self.previous_positions.append(self.logical_position)
        self.previous_velocities.append(self.velocity)

        self.velocity = math.Vector2(
            (self.center.x - x) / constants.STRIKE_SCALE_FACTOR,
            (self.center.y - y) / constants.STRIKE_SCALE_FACTOR
        )

        if self.velocity.length_squared() >= constants.MAX_SPEED_SQUARED:
            self.velocity.scale_to_length(constants.MAX_SPEED)

    def stop(self):
        self.previous_velocities.append(self.velocity)
        self.velocity = math.Vector2(0, 0)
