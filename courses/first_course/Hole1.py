
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
    ball=Point(540, 520, 0),
    noncollidibles=LayeredDirty(
        Text(Point(720, 180), 'Par 1', font.Font(None, 30), colors.WHITE)
    ),
    collidibles=LayeredDirty(
        Green(Point(380, 120, 0), Point(710, 570, 0)),
        Pin(Point(540, 180, 0)),
        Wall(Point(380, 120, 0), Point(710, 120, 0), 5),
        Wall(Point(710, 120, 0), Point(710, 570, 0), 5),
        Wall(Point(710, 570, 0), Point(380, 570, 0), 5),
        Wall(Point(380, 570, 0), Point(380, 120, 0), 5)
    )
)
