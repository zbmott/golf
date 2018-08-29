
from pygame import Color, font
from pygame.math import Vector2
from pygame.sprite import LayeredDirty

from src.models import Hole as BaseHole
from src.sprites import *
from src.utils import colors, Point


Hole = BaseHole(
    'Hole #5',
    par=4,
    origin=Point(50, 100, 0),
    ball=Point(490, 550, 0),
    noncollidibles=LayeredDirty(
        Text(Point(670, 138), 'Par 4', font.Font(None, 30), colors.WHITE),
    ),
    collidibles=LayeredDirty(
        Green([Point(440, 100, 0), Point(540, 100, 0), Point(540, 200, 0), Point(440, 200, 0)]),
        Slope([Point(440, 100, 0), Point(380, 50, 0), Point(600, 50, 0), Point(540, 100, 0)], Color(100, 0, 0, 255), Vector2(0.0, -0.4)),
        Slope([Point(600, 50, 0), Point(540, 100, 0), Point(540, 200, 0), Point(600, 250, 0)], Color(100, 0, 0, 255), Vector2(0.4, 0.0)),
        Slope([Point(600, 250, 0), Point(540, 200, 0), Point(440, 200, 0), Point(380, 250, 0)], Color(100, 0, 0, 255), Vector2(0.0, 0.4)),
        Slope([Point(380, 250, 0), Point(440, 200, 0), Point(440, 100, 0), Point(380, 50, 0)], Color(100, 0, 0, 255), Vector2(-0.4, 0.0)),
        Rough([Point(380, 50, 0), Point(380, 10, 0), Point(600, 10, 0), Point(600, 50, 0)]),
        Rough([Point(600, 10, 0), Point(640, 10, 0), Point(640, 250, 0), Point(600, 250, 0)]),
        Rough([Point(640, 250, 0), Point(640, 290, 0), Point(380, 290, 0), Point(380, 250, 0)]),
        Rough([Point(380, 290, 0), Point(340, 290, 0), Point(340, 10, 0), Point(380, 10, 0)]),
        Green([Point(420, 290, 0), Point(560, 290, 0), Point(560, 590, 0), Point(420, 590, 0)]),
        Pin(Point(490, 150, 0)),
        Money(Point(440, 315)),
        Wall(Point(340, 10, 0), Point(640, 10, 0), 5),
        Wall(Point(640, 10, 0), Point(640, 290, 0), 5),
        Wall(Point(340, 10, 0), Point(340, 290, 0), 5),
        Wall(Point(340, 290, 0), Point(420, 290, 0), 5),
        Wall(Point(640, 290, 0), Point(560, 290, 0), 5),
        Wall(Point(420, 290, 0), Point(420, 590, 0), 5),
        Wall(Point(420, 590, 0), Point(560, 590, 0), 5),
        Wall(Point(560, 590, 0), Point(560, 290, 0), 5)
    )
)
