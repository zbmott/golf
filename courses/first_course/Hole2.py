
from pygame import Color, font
from pygame.math import Vector2
from pygame.sprite import LayeredDirty

from src.models import Hole as BaseHole
from src.sprites import *
from src.utils import colors, Point


Hole = BaseHole(
    'Hole #2',
    par=2,
    origin=Point(50, 50, 0),
    ball=Point(390, 575, 0),
    noncollidibles=LayeredDirty(
        Text(Point(670, 140), 'Par 2', font.Font(None, 30), colors.WHITE)
    ),
    collidibles=LayeredDirty(
        Green([Point(440, 210, 0), Point(540, 210, 0), Point(540, 510, 0), Point(640, 510, 0), Point(640, 630, 0), Point(340, 630, 0), Point(340, 510, 0), Point(440, 510, 0)]),
        Rough([Point(440, 210, 0), Point(340, 210, 0), Point(340, 90, 0), Point(640, 90, 0), Point(640, 210, 0)]),
        Pin(Point(600, 150, 0)),
        Wall(Point(340, 90, 0), Point(640, 90, 0), 5),
        Wall(Point(640, 90, 0), Point(640, 210, 0), 5),
        Wall(Point(640, 210, 0), Point(540, 210, 0), 5),
        Wall(Point(540, 210, 0), Point(540, 510, 0), 5),
        Wall(Point(540, 510, 0), Point(640, 510, 0), 5),
        Wall(Point(640, 510, 0), Point(640, 630, 0), 5),
        Wall(Point(640, 630, 0), Point(340, 630, 0), 5),
        Wall(Point(340, 630, 0), Point(340, 510, 0), 5),
        Wall(Point(340, 510, 0), Point(440, 510, 0), 5),
        Wall(Point(440, 510, 0), Point(440, 210, 0), 5),
        Wall(Point(440, 210, 0), Point(340, 210, 0), 5),
        Wall(Point(340, 210, 0), Point(340, 90, 0), 5)
    )
)
