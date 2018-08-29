
from pygame import Color, font
from pygame.math import Vector2
from pygame.sprite import LayeredDirty

from src.models import Hole as BaseHole
from src.sprites import *
from src.utils import colors, Point


Hole = BaseHole(
    'Hole #4',
    par=4,
    origin=Point(50, 100, 0),
    ball=Point(312, 580, 0),
    noncollidibles=LayeredDirty(
        Text(Point(900, 268), 'Par 4', font.Font(None, 30), colors.WHITE),
    ),
    collidibles=LayeredDirty(
        Green([Point(250, 600, 0), Point(250, 150, 0), Point(370, 150, 0), Point(370, 250, 0), Point(770, 250, 0), Point(770, 150, 0), Point(870, 150, 0), Point(870, 400, 0), Point(770, 400, 0), Point(770, 300, 0), Point(370, 300, 0), Point(370, 600, 0)]),
        Slope([Point(250, 150, 0), Point(250, 90, 0), Point(370, 90, 0), Point(370, 150, 0)], Color(100, 0, 0, 255), Vector2(0.0, -0.7)),
        Sand([Point(250, 90, 0), Point(250, 50, 0), Point(370, 50, 0), Point(370, 90, 0)]),
        Slope([Point(410, 250, 0), Point(410, 200, 0), Point(770, 200, 0), Point(770, 250, 0)], Color(100, 0, 0, 255), Vector2(-0.33, -0.6)),
        Slope([Point(410, 300, 0), Point(410, 360, 0), Point(770, 360, 0), Point(770, 300, 0)], Color(100, 0, 0, 255), Vector2(-0.33, 0.6)),
        Rough([Point(410, 200, 0), Point(410, 150, 0), Point(770, 150, 0), Point(770, 200, 0)]),
        Rough([Point(770, 400, 0), Point(410, 400, 0), Point(410, 360, 0), Point(770, 360, 0)]),
        Pin(Point(840, 275, 0)),
        Money(Point(305, 200)),
        Wall(Point(250, 50, 0), Point(370, 50, 0), 5),
        Wall(Point(370, 50, 0), Point(370, 250, 0), 5),
        Wall(Point(370, 250, 0), Point(410, 250, 0), 5),
        Wall(Point(410, 250, 0), Point(410, 150, 0), 5),
        Wall(Point(410, 150, 0), Point(870, 150, 0), 5),
        Wall(Point(870, 150, 0), Point(870, 400, 0), 5),
        Wall(Point(870, 400, 0), Point(410, 400, 0), 5),
        Wall(Point(410, 400, 0), Point(410, 300, 0), 5),
        Wall(Point(410, 300, 0), Point(370, 300, 0), 5),
        Wall(Point(370, 300, 0), Point(370, 600, 0), 5),
        Wall(Point(370, 600, 0), Point(250, 600, 0), 5),
        Wall(Point(250, 600, 0), Point(250, 50, 0), 5)
    )
)
