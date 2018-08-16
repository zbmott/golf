
from pygame import Color, font
from pygame.math import Vector2
from pygame.sprite import LayeredDirty

from src.models import Hole as BaseHole
from src.sprites import *
from src.utils import colors, Point


Hole = BaseHole(
    'Hole #5',
    par=3,
    origin=Point(50, 50, 0),
    ball=Point(480, 650, 0),
    noncollidibles=LayeredDirty(
        Text(Point(640, 190), 'Par 3', font.Font(None, 30), colors.WHITE),
    ),
    collidibles=LayeredDirty(
        Green(Point(460, 170, 0), Point(520, 230, 0)),
        Slope(Point(460, 80, 0), Point(520, 170, 0), Color(100, 0, 0, 255), Vector2(0.0, -0.33)),
        Slope(Point(520, 80, 0), Point(570, 170, 0), Color(100, 0, 0, 255), Vector2(0.33, -0.33)),
        Slope(Point(520, 170, 0), Point(570, 230, 0), Color(100, 0, 0, 255), Vector2(0.33, 0.0)),
        Slope(Point(520, 230, 0), Point(570, 320, 0), Color(100, 0, 0, 255), Vector2(0.33, 0.33)),
        Slope(Point(460, 230, 0), Point(520, 320, 0), Color(100, 0, 0, 255), Vector2(0.0, 0.33)),
        Slope(Point(400, 230, 0), Point(460, 320, 0), Color(100, 0, 0, 255), Vector2(-0.33, 0.33)),
        Slope(Point(400, 170, 0), Point(460, 230, 0), Color(100, 0, 0, 255), Vector2(-0.33, 0.0)),
        Slope(Point(400, 80, 0), Point(460, 170, 0), Color(100, 0, 0, 255), Vector2(-0.33, -0.33)),
        Rough(Point(340, 30, 0), Point(630, 80, 0)),
        Rough(Point(570, 80, 0), Point(630, 370, 0)),
        Rough(Point(340, 80, 0), Point(400, 320, 0)),
        Rough(Point(340, 320, 0), Point(400, 370, 0)),
        Rough(Point(400, 320, 0), Point(570, 690, 0)),
        Pin(Point(478, 188, 0)),
        Wall(Point(340, 30, 0), Point(630, 30, 0), 5),
        Wall(Point(630, 30, 0), Point(630, 370, 0), 5),
        Wall(Point(630, 370, 0), Point(570, 370, 0), 5),
        Wall(Point(570, 370, 0), Point(570, 690, 0), 5),
        Wall(Point(570, 690, 0), Point(400, 690, 0), 5),
        Wall(Point(400, 690, 0), Point(400, 370, 0), 5),
        Wall(Point(400, 370, 0), Point(340, 370, 0), 5),
        Wall(Point(340, 370, 0), Point(340, 30, 0), 5)
    )
)
