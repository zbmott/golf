# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

from src.utils.colors import GREEN
from .FrictionalSurface import FrictionalSurface


class Green(FrictionalSurface):
    def __init__(self, point, width, height, *groups):
        super().__init__(point, width, height, GREEN, 0.98, *groups)
