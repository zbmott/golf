# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

from src.utils.colors import DARKGREEN
from .FrictionalSurface import FrictionalSurface


class Rough(FrictionalSurface):
    def __init__(self, point, width, height, *groups):
        super().__init__(point, width, height, DARKGREEN, 0.945, *groups)
