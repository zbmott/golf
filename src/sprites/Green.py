# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

from .FrictionalSurface import FrictionalSurface


class Green(FrictionalSurface):
    GREEN = (0, 100, 0)

    def __init__(self, point, width, height, *groups):
        super().__init__(point, width, height, self.GREEN, 0.98, *groups)
