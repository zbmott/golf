# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

from src.utils import colors
from .abstract import FrictionalSurface


class Rough(FrictionalSurface):
    def __init__(self, points, *groups):
        super().__init__(points, colors.DARKGREEN, 0.945, *groups)

    def __repr__(self):
        points = ', '.join([repr(p) for p in self.points])
        return "Rough([{points}])".format(points=points)
