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
    noncollidibles=Group(
        Text(Point(810, 143), 'Par 2', font.Font(None, 30), colors.WHITE),
    ),
    collidibles=Group(
        Rough(Point(490, 80), 300, 150),
        Green(Point(590, 230), 100, 400),
        Green(Point(490, 630), 300, 150),

        Wall(Point(490, 80), Point(790, 80), 5),
        Wall(Point(490, 80), Point(490, 230), 5),
        Wall(Point(790, 80), Point(790, 230), 5),
        Wall(Point(490, 230), Point(590, 230), 5),
        Wall(Point(690, 230), Point(790, 230), 5),
        Wall(Point(590, 230), Point(590, 630), 5),
        Wall(Point(690, 230), Point(690, 630), 5),
        Wall(Point(490, 630), Point(590, 630), 5),
        Wall(Point(690, 630), Point(790, 630), 5),
        Wall(Point(490, 630), Point(490, 780), 5),
        Wall(Point(490, 780), Point(790, 780), 5),
        Wall(Point(790, 630), Point(790, 780), 5),

        Pin(Point(728, 143)),
    ),
    ball=Group(
        GolfBall(Point(530, 715))
    ),
)
