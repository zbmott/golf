
from pygame import Color, font
from pygame.math import Vector2
from pygame.sprite import LayeredDirty

from src.models import Hole as BaseHole
from src.sprites import *
from src.utils import colors, Point


Hole = BaseHole(
    'Hole #7',
    par=4,
    origin=Point(50, 50, 0),
    ball=Point(255, 630, 0),
    noncollidibles=LayeredDirty(
        Text(Point(805, 70), 'Par 4', font.Font(None, 30), colors.WHITE)
    ),
    collidibles=LayeredDirty(
        Green([Point(50, 500, 0), Point(450, 500, 0), Point(450, 700, 0), Point(50, 700, 0)]),
        Slope([Point(200, 500, 0), Point(300, 500, 0), Point(300, 325, 0), Point(200, 325, 0)], Color(125, 0, 0, 255), Vector2(0.0, -0.1)),
        Rough([Point(200, 325, 0), Point(200, 200, 0), Point(300, 200, 0), Point(300, 325, 0)]),
        Slope([Point(200, 200, 0), Point(200, 100, 0), Point(300, 10, 0), Point(300, 200, 0)], Color(125, 0, 0, 255), Vector2(0.0, -0.15)),
        Green([Point(300, 100, 0), Point(600, 100, 0), Point(600, 10, 0), Point(300, 10, 0)]),
        Slope([Point(600, 100, 0), Point(700, 100, 0), Point(600, 10, 0)], Color(125, 0, 0, 255), Vector2(0.05, 0.15)),
        Slope([Point(600, 100, 0), Point(600, 200, 0), Point(700, 200, 0), Point(700, 100, 0)], Color(125, 0, 0, 255), Vector2(0.0, 0.25)),
        Green([Point(300, 200, 0), Point(700, 200, 0), Point(750, 200, 0), Point(750, 100, 0), Point(900, 100, 0), Point(900, 400, 0), Point(750, 400, 0), Point(750, 300, 0), Point(300, 300, 0)]),
        Green([Point(600, 300, 0), Point(700, 300, 0), Point(700, 500, 0), Point(600, 420, 0), Point(600, 300, 0)]),
        Slope([Point(700, 500, 0), Point(600, 500, 0), Point(600, 420, 0)], Color(125, 0, 0, 255), Vector2(0.2, -0.1)),
        Green([Point(700, 400, 0), Point(900, 400, 0), Point(900, 500, 0), Point(700, 500, 0)]),
        Rough([Point(900, 100, 0), Point(950, 100, 0), Point(950, 500, 0), Point(900, 500, 0)]),
        Water([Point(950, 100, 0), Point(1070, 100, 0), Point(1070, 500, 0), Point(950, 500, 0)]),
        Pin(Point(830, 250, 0)),
        Money(Point(820, 440)),
        Wall(Point(50, 500, 0), Point(200, 500, 0), 5),
        Wall(Point(200, 500, 0), Point(200, 100, 0), 5),
        Wall(Point(300, 10, 0), Point(200, 100, 0),  5),
        Wall(Point(300, 10, 0), Point(600, 10, 0), 5),
        Wall(Point(700, 100, 0), Point(600, 10, 0), 5),
        Wall(Point(700, 100, 0), Point(700, 200, 0), 5),
        Wall(Point(700, 200, 0), Point(750, 200, 0), 5),
        Wall(Point(750, 200, 0), Point(750, 100, 0), 5),
        Wall(Point(750, 100, 0), Point(1070, 100, 0), 5),
        Wall(Point(1070, 100, 0), Point(1070, 500, 0), 5),
        Wall(Point(1070, 500, 0), Point(600, 500, 0), 5),
        Wall(Point(600, 500, 0), Point(600, 300, 0), 5),
        Wall(Point(600, 300, 0), Point(300, 300, 0), 5),
        Wall(Point(300, 300, 0), Point(300, 500, 0), 5),
        Wall(Point(300, 500, 0), Point(450, 500, 0), 5),
        Wall(Point(450, 500, 0), Point(450, 700, 0), 5),
        Wall(Point(450, 700, 0), Point(50, 700, 0), 5),
        Wall(Point(50, 700, 0), Point(50, 500, 0), 5),
        Wall(Point(300, 100, 0), Point(600, 100, 0), 5),
        Wall(Point(600, 100, 0), Point(600, 200, 0), 5),
        Wall(Point(600, 200, 0), Point(300, 200, 0), 5),
        Wall(Point(300, 200, 0), Point(300, 100, 0), 5),
        Wall(Point(700, 300, 0), Point(750, 300, 0), 5),
        Wall(Point(750, 300, 0), Point(750, 400, 0), 5),
        Wall(Point(750, 400, 0), Point(700, 400, 0), 5),
        Wall(Point(700, 400, 0), Point(700, 300, 0), 5)
    )
)
