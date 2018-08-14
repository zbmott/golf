# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

from .FrictionalSurface import FrictionalSurface


class Sand(FrictionalSurface):
    SANDY = (249, 249, 121)

    def __init__(self, point, width, height, *groups):
        super().__init__(point, width, height, self.SANDY, 0.875, *groups)
