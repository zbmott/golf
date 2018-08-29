
from pygame import Color, font
from pygame.math import Vector2
from pygame.sprite import LayeredDirty

from src.models import Hole as BaseHole
from src.sprites import *
from src.utils import colors, Point


Hole = BaseHole(
    'Hole #3',
    par=3,
    origin=Point(50, 50, 0),
    ball=Point(253, 555, 0),
    noncollidibles=LayeredDirty(
        Text(Point(850, 183), 'Par 3', font.Font(None, 30), colors.WHITE)
    ),
    collidibles=LayeredDirty(
        Green([Point(180, 140, 0), Point(830, 140, 0), Point(830, 240, 0), Point(310, 240, 0), Point(310, 590, 0), Point(180, 590, 0)]),
        Rough([Point(310, 240, 0), Point(380, 240, 0), Point(380, 590, 0), Point(310, 590, 0)]),
        Sand([Point(380, 240, 0), Point(830, 240, 0), Point(830, 310, 0), Point(380, 310, 0)]),
        Pin(Point(780, 190, 0)),
        Money(Point(773, 265)),
        Wall(Point(180, 140, 0), Point(830, 140, 0), 5),
        Wall(Point(830, 140, 0), Point(830, 310, 0), 5),
        Wall(Point(830, 310, 0), Point(380, 310, 0), 5),
        Wall(Point(380, 310, 0), Point(380, 590, 0), 5),
        Wall(Point(380, 590, 0), Point(180, 590, 0), 5),
        Wall(Point(180, 590, 0), Point(180, 140, 0), 5)
    )
)
