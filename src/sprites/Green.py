# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

from src.utils import colors, Point
from .abstract import FrictionalSurface


class Green(FrictionalSurface):
    def __init__(self, points, *groups):
        super().__init__(points, colors.GREEN, 0.98, *groups)
