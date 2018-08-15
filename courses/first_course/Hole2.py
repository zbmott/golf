# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

from pygame import font
from pygame.sprite import Group

from src.models import Hole
from src.sprites import *
from src.utils import colors, Point


Hole2 = Hole(
    'Hole #2',
    par=3,
    origin=Point(100, 100),
    noncollidibles=Group(
        Text(Point(880, 50), 'Par 3', font.Font(None, 30), colors.WHITE),
    ),
    collidibles=Group(
        Green(Point(0, 0), 850, 125),
        Green(Point(0, 125), 150, 500),
        Sand(Point(225, 125), 625, 75),
        Rough(Point(150, 125), 75, 500),

        Wall(Point(0, 0), Point(850, 0), 5),
        Wall(Point(850, 0), Point(850, 200), 5),
        Wall(Point(225, 200), Point(850, 200), 5),
        Wall(Point(225, 200), Point(225, 625), 5),
        Wall(Point(0, 625), Point(225, 625), 5),
        Wall(Point(0, 0), Point(0, 625), 5),

        Pin(Point(800, 50)),
    ),
    ball=Group(
        GolfBall(Point(75, 575))
    ),
)
