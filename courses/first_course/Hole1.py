
from pygame import Color, font
from pygame.math import Vector2
from pygame.sprite import LayeredDirty

from src.models import Hole as BaseHole
from src.sprites import *
from src.utils import colors, Point


Hole = BaseHole(
    'Hole #1',
    par=1,
    origin=Point(50, 50, 0),
    ball=Point(535, 545, 0),
    noncollidibles=LayeredDirty(
        Text(Point(515, 160), 'Par 1', font.Font(None, 30), colors.WHITE),
    ),
    collidibles=LayeredDirty(
        Green([Point(360, 190, 0), Point(700, 190, 0), Point(700, 600, 0), Point(360, 600, 0)]),
        Pin(Point(535, 260, 0)),
        Money(Point(529, 215)),
        Wall(Point(360, 190, 0), Point(700, 190, 0), 5),
        Wall(Point(700, 190, 0), Point(700, 600, 0), 5),
        Wall(Point(700, 600, 0), Point(360, 600, 0), 5),
        Wall(Point(360, 600, 0), Point(360, 190, 0), 5)
    )
)
