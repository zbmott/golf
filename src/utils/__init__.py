# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

from pygame.mask import Mask
from pygame.math import Vector2

__all__ = [
    'Point'
]


def round_(n, base=10):
    return int(base * round(float(n) / base))


def create_rectangular_mask(canvas_width, canvas_height, offset_x, offset_y, mask_width, mask_height):
    m = Mask((canvas_width, canvas_height))

    for x in range(offset_x, offset_x + mask_width):
        for y in range(offset_y, offset_y + mask_height):
            m.set_at((x, y), 1)

    return m


class Point(object):
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        elif item == 2:
            return self.z

        raise IndexError('Point only has x, y, and z coordinates.')

    def as_2d_tuple(self):
        return self.x, self.y

    def as_3d_tuple(self):
        return self.x, self.y, self.z

    def __repr__(self):
        return "Point({self.x!r}, {self.y!r}, {self.z!r})".format(self=self)

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, Vector2):
            return Point(self.x + other.x, self.y + other.y, self.z)

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, Vector2):
            return Point(self.x - other.x, self.y - other.y, self.z)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y and self.z == other.z

        raise ValueError('Points can only be compared to other Points.')
