# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

from src.utils import colors
from .abstract import FrictionalSurface


class Sand(FrictionalSurface):
    def __init__(self, points, *groups):
        super().__init__(points, colors.SANDY, 0.875, *groups)
