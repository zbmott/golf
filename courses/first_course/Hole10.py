
from pygame import Color, font
from pygame.math import Vector2
from pygame.sprite import LayeredDirty

from src.models import Hole as BaseHole
from src.sprites import *
from src.utils import colors, Point


Hole = BaseHole(
    'Hole #10',
    par=5,
    origin=Point(80, 30, 0),
    ball=Point(440, 125, 0),
    noncollidibles=LayeredDirty(
        Text(Point(530, 15), 'Par 5', font.Font(None, 30), colors.WHITE),
    ),
    collidibles=LayeredDirty(
        Green([Point(50, 50, 0), Point(500, 50, 0), Point(500, 200, 0), Point(100, 200, 0), Point(100, 450, 0), Point(50, 450, 0)]),
        Slope([Point(100, 200, 0), Point(200, 200, 0), Point(200, 450, 0), Point(100, 450, 0)], Color(200, 0, 0, 255), Vector2(0.3, 0.0)),
        Sand([Point(310, 290, 0), Point(370, 290, 0), Point(370, 350, 0), Point(310, 350, 0)]),
        Slope([Point(200, 200, 0), Point(340, 200, 0), Point(340, 290, 0), Point(310, 290, 0), Point(310, 320, 0), Point(200, 320, 0)], Color(200, 0, 0, 255), Vector2(0.25, 0.25)),
        Slope([Point(340, 200, 0), Point(340, 290, 0), Point(370, 290, 0), Point(370, 320, 0), Point(500, 320, 0), Point(500, 200, 0)], Color(200, 0, 0, 255), Vector2(-0.25, 0.25)),
        Slope([Point(200, 320, 0), Point(310, 320, 0), Point(310, 350, 0), Point(340, 350, 0), Point(340, 450, 0), Point(200, 450, 0)], Color(200, 0, 0, 255), Vector2(0.25, -0.25)),
        Slope([Point(370, 320, 0), Point(500, 320, 0), Point(500, 450, 0), Point(340, 450, 0), Point(340, 350, 0), Point(370, 350, 0)], Color(200, 0, 0, 255), Vector2(-0.25, -0.25)),
        Green([Point(740, 630, 0), Point(890, 630, 0), Point(890, 780, 0), Point(740, 780, 0)]),
        Rough([Point(530, 50, 0), Point(530, 200, 0), Point(630, 200, 0), Point(630, 50, 0)]),
        Green([Point(630, 100, 0), Point(1020, 100, 0), Point(1020, 150, 0), Point(630, 150, 0)]),
        Green([Point(970, 150, 0), Point(640, 230, 0), Point(640, 280, 0), Point(1020, 180, 0), Point(1020, 150, 0)]),
        Green([Point(640, 280, 0), Point(710, 260, 0), Point(860, 630, 0), Point(790, 630, 0)]),
        Sand([Point(1020, 100, 0), Point(1050, 100, 0), Point(1050, 180, 0), Point(1020, 180, 0)]),
        Rough([Point(250, 540, 0), Point(250, 510, 0), Point(50, 510, 0), Point(50, 640, 0), Point(250, 640, 0)]),
        Green([Point(740, 630, 0), Point(650, 630, 0), Point(650, 700, 0), Point(740, 700, 0)]),
        Green([Point(650, 700, 0), Point(340, 610, 0), Point(250, 610, 0), Point(250, 540, 0), Point(330, 540, 0), Point(650, 630, 0)]),
        Water([Point(630, 50, 0), Point(1050, 50, 0), Point(1050, 100, 0), Point(630, 100, 0)]),
        Water([Point(760, 630, 0), Point(500, 450, 0), Point(500, 50, 0), Point(530, 50, 0), Point(530, 200, 0), Point(630, 200, 0), Point(630, 150, 0), Point(970, 150, 0), Point(640, 230, 0), Point(640, 280, 0), Point(790, 630, 0)]),
        Lava([Point(760, 630, 0), Point(500, 450, 0), Point(50, 450, 0), Point(50, 510, 0), Point(250, 510, 0), Point(250, 540, 0), Point(330, 540, 0), Point(650, 630, 0), Point(760, 630, 0)]),
        Water([Point(890, 750, 0), Point(1050, 750, 0), Point(1050, 850, 0), Point(820, 850, 0), Point(820, 780, 0), Point(890, 780, 0)]),
        Lava([Point(820, 850, 0), Point(820, 780, 0), Point(740, 780, 0), Point(740, 700, 0), Point(650, 700, 0), Point(340, 610, 0), Point(250, 610, 0), Point(250, 640, 0), Point(50, 640, 0), Point(50, 850, 0)]),
        Lava([Point(890, 750, 0), Point(890, 630, 0), Point(1050, 630, 0), Point(1050, 750, 0)]),
        Water([Point(710, 260, 0), Point(1020, 180, 0), Point(1050, 180, 0), Point(1050, 630, 0), Point(860, 630, 0)]),
        Pin(Point(825, 675, 0)),
        Tunnel(Point(340, 320, 0), Point(540, 120, 0), Vector2(2.5, 0.0)),
        Tunnel(Point(77, 425, 0), Point(70, 580, 0), Vector2(5.0, 0.0)),
        Wall(Point(50, 50, 0), Point(1050, 50, 0), 10),
        Wall(Point(1050, 50, 0), Point(1050, 850, 0), 10),
        Wall(Point(1050, 850, 0), Point(50, 850, 0), 10),
        Wall(Point(50, 850, 0), Point(50, 50, 0), 10),
        Wall(Point(50, 450, 0), Point(500, 450, 0), 10),
        Wall(Point(500, 450, 0), Point(500, 50, 0), 10)
    )
)
