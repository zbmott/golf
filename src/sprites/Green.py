# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

from src.utils import colors, Point
from .FrictionalSurface import FrictionalSurface


class Green(FrictionalSurface):
    def __init__(self, point1, point2, *groups):
        super().__init__(point1, point2, colors.GREEN, 0.98, *groups)

    def __repr__(self):
        p1 = Point(self.rect.x, self.rect.y)
        p2 = Point(self.rect.x + self.rect.width, self.rect.y + self.rect.height)
        return "Green({p1!r}, {p2!r})".format(p1=p1, p2=p2)
