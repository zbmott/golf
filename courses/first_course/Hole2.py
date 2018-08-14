# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

from pygame.sprite import Group

from src.models import Hole
from src.sprites import *
from src.utils import Point


Hole2 = Hole(
    'Hole #2',
    par=4,
    collidibles=Group(
        Green(Point(150, 75), 850, 125),
        Green(Point(150, 200), 150, 500),
        Sand(Point(375, 200), 625, 75),
        Rough(Point(300, 200), 75, 500),

        Wall(Point(150, 75), Point(1000, 75), 3),
        Wall(Point(1000, 75), Point(1000, 275), 3),
        Wall(Point(375, 275), Point(1000, 275), 5),
        Wall(Point(375, 275), Point(375, 700), 5),
        Wall(Point(150, 700), Point(375, 700), 3),
        Wall(Point(150, 75), Point(150, 700), 3),

        Pin(Point(950, 125)),
    ),
    ball=Group(
        GolfBall(Point(225, 650))
    ),
)