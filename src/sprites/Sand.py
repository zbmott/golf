# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

from src.utils.colors import SANDY
from .FrictionalSurface import FrictionalSurface


class Sand(FrictionalSurface):
    def __init__(self, point, width, height, *groups):
        super().__init__(point, width, height, SANDY, 0.875, *groups)
