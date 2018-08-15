# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

from os import path

from pygame import math

from src.utils import Point
from .ImageSprite import ImageSprite


class GolfBall(ImageSprite):
    RADIUS = 10
    IMAGE_PATH = path.join(
        path.dirname(path.dirname(path.dirname(__file__))),
        'assets',
        'golfball_20x20.png'
    )
    MAX_SPEED = 15
    MAX_SPEED_SQUARED = MAX_SPEED**2
    STRIKE_SCALE_FACTOR = 7.5

    def __init__(self, point, *groups):
        super().__init__(*groups)

        self.velocity = math.Vector2(0, 0)

        self.logical_position = Point(point.x - self.RADIUS, point.y - self.RADIUS)

        self.rect.x = self.logical_position.x
        self.rect.y = self.logical_position.y

    @property
    def center(self):
        return Point(
            int(self.logical_position.x + self.RADIUS),
            int(self.logical_position.y + self.RADIUS)
        )

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
        self.velocity = math.Vector2(
            (self.center.x - x) / self.STRIKE_SCALE_FACTOR,
            (self.center.y - y) / self.STRIKE_SCALE_FACTOR
        )

        if self.velocity.length_squared() >= self.MAX_SPEED_SQUARED:
            self.velocity.scale_to_length(self.MAX_SPEED)

    def stop(self):
        self.velocity.x = 0
        self.velocity.y = 0

    def collide(self, collidibles):
        collisions = []

        for collidible in collidibles.sprites():
            if self.rect.collidelist(collidible.collision_rects) != -1:
                collisions.append(collidible)

        return collisions
