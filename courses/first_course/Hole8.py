
from pygame import Color, font
from pygame.math import Vector2
from pygame.sprite import LayeredDirty

from src.models import Hole as BaseHole
from src.sprites import *
from src.utils import colors, Point


Hole = BaseHole(
    'Hole #8',
    par=2,
    origin=Point(50, 50, 0),
    ball=Point(145, 520, 0),
    noncollidibles=LayeredDirty(
        Text(Point(708, 20), 'Par 2', font.Font(None, 30), colors.WHITE),
        Text(Point(925, 310), 'Is this lava?', font.Font(None, 24), colors.WHITE)
    ),
    collidibles=LayeredDirty(
        Green([Point(50, 50, 0), Point(50, 580, 0), Point(250, 580, 0), Point(250, 200, 0), Point(650, 200, 0), Point(650, 50, 0)]),
        Rough([Point(650, 50, 0), Point(800, 50, 0), Point(800, 200, 0), Point(650, 200, 0)]),
        Lava([Point(250, 580, 0), Point(250, 200, 0), Point(800, 200, 0), Point(800, 50, 0), Point(900, 50, 0), Point(900, 580, 0)]),
        Pin(Point(730, 125, 0)),
        Money(Point(225, 175)),
        Wall(Point(50, 50, 0), Point(900, 50, 0), 5),
        Wall(Point(900, 50, 0), Point(900, 580, 0), 5),
        Wall(Point(900, 580, 0), Point(50, 580, 0), 5),
        Wall(Point(50, 580, 0), Point(50, 50, 0), 5)
    )
)
