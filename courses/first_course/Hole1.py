# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

from pygame import font
from pygame.sprite import Group

from src.models import Hole
from src.sprites import *
from src.utils import colors, Point


Hole1 = Hole(
    'Hole #1',
    par=2,
    origin=Point(100, 100),
    noncollidibles=Group(
        Text(Point(710, 63), 'Par 2', font.Font(None, 30), colors.WHITE),
    ),
    collidibles=Group(
        Rough(Point(390, 0), 300, 150),
        Green(Point(490, 150), 100, 400),
        Green(Point(390, 550), 300, 150),

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
    ball=Group(
        GolfBall(Point(430, 635))
    ),
)
