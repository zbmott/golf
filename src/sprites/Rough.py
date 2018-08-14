# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

from .FrictionalSurface import FrictionalSurface


class Rough(FrictionalSurface):
    DARK_GREEN = (0, 70, 0)

    def __init__(self, point, width, height, *groups):
        super().__init__(point, width, height, self.DARK_GREEN, 0.945, *groups)
