
from pygame import Color, font
from pygame.math import Vector2
from pygame.sprite import LayeredDirty

from src.models import Hole as BaseHole
from src.sprites import *
from src.utils import colors, Point


Hole = BaseHole(
    'Hole #6',
    par=3,
    origin=Point(150, 100, 0),
    ball=Point(200, 630, 0),
    noncollidibles=LayeredDirty(
        Text(Point(88, 92), 'Par 3', font.Font(None, 30), colors.WHITE)
    ),
    collidibles=LayeredDirty(
        Water([Point(150, 150, 0), Point(150, 550, 0), Point(550, 550, 0), Point(550, 150, 0)]),
        Green([Point(150, 550, 0), Point(550, 550, 0), Point(550, 700, 0), Point(150, 700, 0)]),
        Green([Point(150, 150, 0), Point(150, 50, 0), Point(550, 50, 0), Point(550, 150, 0)]),
        Green([Point(550, 700, 0), Point(610, 550, 0), Point(550, 550, 0)]),
        Slope([Point(550, 700, 0), Point(610, 550), Point(700, 550, 0), Point(700, 700, 0)], Color(125, 0, 0, 255), Vector2(0.01, -0.5)),
        Sand([Point(550, 150, 0), Point(610, 150, 0), Point(610, 550, 0), Point(550, 550, 0)]),
        Slope([Point(700, 550, 0), Point(700, 150, 0), Point(610, 150, 0), Point(610, 550, 0)], Color(125, 0, 0, 255), Vector2(-0.15, 0.0)),
        Rough([Point(550, 50, 0), Point(700, 50, 0), Point(700, 150, 0), Point(550, 150)]),
        Pin(Point(200, 100, 0)),
        Money(Point(640, 650)),
        Wall(Point(150, 50, 0), Point(700, 50, 0), 5),
        Wall(Point(700, 50, 0), Point(700, 700, 0), 5),
        Wall(Point(700, 700, 0), Point(150, 700, 0), 5),
        Wall(Point(150, 700, 0), Point(150, 50, 0), 5)
    )
)
