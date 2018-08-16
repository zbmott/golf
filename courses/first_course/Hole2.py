# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

from pygame import font
from pygame.sprite import LayeredDirty

from src.models import Hole as BaseHole
from src.sprites import *
from src.utils import colors, Point

__all__ = ['Hole']


Hole = BaseHole(
    'Hole #2',
    par=2,
    origin=Point(100, 100),
    ball=Point(430, 635),
    noncollidibles=LayeredDirty(
        Text(Point(710, 63), 'Par 2', font.Font(None, 30), colors.WHITE),
    ),
    collidibles=LayeredDirty(
        Rough(Point(390, 0), Point(690, 150)),
        Green(Point(490, 150), Point(590, 550)),
        Green(Point(390, 550), Point(690, 700)),

        Wall(Point(390, 0), Point(690, 0), 5),
        Wall(Point(390, 0), Point(390, 150), 5),
        Wall(Point(690, 0), Point(690, 150), 5),
        Wall(Point(390, 150), Point(490, 150), 5),
        Wall(Point(590, 150), Point(690, 150), 5),
        Wall(Point(490, 150), Point(490, 550), 5),
        Wall(Point(590, 150), Point(590, 550), 5),
        Wall(Point(390, 550), Point(490, 550), 5),
        Wall(Point(590, 550), Point(690, 550), 5),
        Wall(Point(390, 550), Point(390, 700), 5),
        Wall(Point(390, 700), Point(690, 700), 5),
        Wall(Point(690, 550), Point(690, 700), 5),

        Pin(Point(628, 63)),
    ),
)
