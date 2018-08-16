
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
    ball=Point(490, 500, 0),
    noncollidibles=LayeredDirty(
        Text(Point(620, 225), 'Par 1', font.Font(None, 30), colors.WHITE)
    ),
    collidibles=LayeredDirty(
        Green([Point(370, 170, 0), Point(600, 170, 0), Point(600, 540, 0), Point(370, 540, 0)]),
        Pin(Point(490, 230, 0)),
        Wall(Point(370, 170, 0), Point(600, 170, 0), 5),
        Wall(Point(600, 170, 0), Point(600, 540, 0), 5),
        Wall(Point(600, 540, 0), Point(370, 540, 0), 5),
        Wall(Point(370, 540, 0), Point(370, 170, 0), 5)
    )
)
