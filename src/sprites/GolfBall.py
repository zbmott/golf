# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

from os import path

from pygame import math, Rect

from src import constants
from src.utils import create_rectangular_mask, Point
from .abstract import ImageSprite


class GolfBall(ImageSprite):
    RADIUS = 10
    IMAGE_PATH = path.join(
        path.dirname(path.dirname(path.dirname(__file__))),
        'assets',
        'golfball_20x20.png'
    )

    def __init__(self, point, funds=0, *groups):
        super().__init__()

        self.funds = funds
        self.points = [point]
        self._layer = constants.LAYER_BALL
        self.add(*groups)

        self._velocity = math.Vector2(0, 0)

        self.logical_position = Point(point.x - self.RADIUS, point.y - self.RADIUS)

        self.rect.x = self.logical_position.x
        self.rect.y = self.logical_position.y

        # This is a special collision mask we use for checks against surfaces.
        # It's a little bit smaller that then the sprite-based collision mask
        # to account for the fact that the ball is, in theory, spherical.
        self.surface_mask = create_rectangular_mask(
            self.rect.width,
            self.rect.height,
            5, 5,
            10, 10
        )

        self.previous_positions = []
        self.previous_velocities = []

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        self.previous_velocities.append(self.velocity)
        self._velocity = value

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

    @classmethod
    def should_finalize(cls, points):
        return len(points) == 2

    def update(self):
        self.logical_position.x += self.velocity.x
        self.logical_position.y += self.velocity.y

        # Update the ball's physical position to match the pixels
        # nearest its logical position.
        self.rect.x = int(self.logical_position.x)
        self.rect.y = int(self.logical_position.y)

    def set_logical_pos(self, point):
        self.logical_position = point

    def center_on(self, point):
        self.set_logical_pos(Point(point.x - self.RADIUS, point.y - self.RADIUS))

    def strike(self, x, y):
        self.previous_positions.append(self.logical_position)

        new_velocity = math.Vector2(
            (self.center.x - x) / constants.STRIKE_SCALE_FACTOR,
            (self.center.y - y) / constants.STRIKE_SCALE_FACTOR
        )

        if new_velocity.length_squared() >= constants.MAX_SPEED_SQUARED:
            new_velocity.scale_to_length(constants.MAX_SPEED)

        self.velocity = new_velocity

    def stop(self):
        self.velocity = math.Vector2(0, 0)
