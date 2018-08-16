
from pygame import Color, font
from pygame.math import Vector2
from pygame.sprite import LayeredDirty

from src.models import Hole as BaseHole
from src.sprites import *
from src.utils import colors, Point


Hole = BaseHole(
    'Hole #4',
    par=4,
    origin=Point(50, 50, 0),
    ball=Point(130, 660, 0),
    noncollidibles=LayeredDirty(
        Text(Point(950, 300), 'Par 4', font.Font(None, 30), colors.WHITE),
    ),
    collidibles=LayeredDirty(
        Green(Point(50, 220, 0), Point(230, 700, 0)),
        Slope(Point(50, 160, 0), Point(230, 220, 0), Color(100, 0, 0, 255), Vector2(0.0, -0.6)),
        Sand(Point(50, 110, 0), Point(230, 160, 0)),
        Green(Point(230, 290, 0), Point(800, 340, 0)),
        Slope(Point(280, 340, 0), Point(800, 410, 0), Color(100, 0, 0, 255), Vector2(-0.25, 0.6)),
        Slope(Point(280, 220, 0), Point(800, 290, 0), Color(100, 0, 0, 255), Vector2(-0.25, -0.6)),
        Rough(Point(280, 410, 0), Point(800, 470, 0)),
        Rough(Point(280, 160, 0), Point(800, 220, 0)),
        Green(Point(800, 160, 0), Point(930, 470, 0)),
        Pin(Point(880, 300, 0)),
        Wall(Point(50, 110, 0), Point(230, 110, 0), 5),
        Wall(Point(230, 110, 0), Point(230, 290, 0), 5),
        Wall(Point(230, 290, 0), Point(280, 290, 0), 5),
        Wall(Point(280, 290, 0), Point(280, 160, 0), 5),
        Wall(Point(280, 160, 0), Point(930, 160, 0), 5),
        Wall(Point(930, 160, 0), Point(930, 470, 0), 5),
        Wall(Point(930, 470, 0), Point(280, 470, 0), 5),
        Wall(Point(280, 470, 0), Point(280, 340, 0), 5),
        Wall(Point(280, 340, 0), Point(230, 340, 0), 5),
        Wall(Point(230, 340, 0), Point(230, 700, 0), 5),
        Wall(Point(230, 700, 0), Point(50, 700, 0), 5),
        Wall(Point(50, 700, 0), Point(50, 110, 0), 5)
    )
)
