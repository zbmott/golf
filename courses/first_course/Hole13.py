
from pygame import Color, font
from pygame.math import Vector2
from pygame.sprite import LayeredDirty

from src.models import Hole as BaseHole
from src.sprites import *
from src.utils import colors, Point



Hole = BaseHole(
    'Hole #13',
    par=3,
    origin=Point(100, 0, 0),
    ball=Point(495, 315, 0),
    noncollidibles=LayeredDirty(
        Text(Point(775, 605), 'Par 3', font.Font(None, 30), colors.WHITE),
    ),
    collidibles=LayeredDirty(
        Green([Point(440, 260, 0), Point(540, 260, 0), Point(540, 360, 0), Point(440, 360, 0)]),
        Slope([Point(440, 360, 0), Point(510, 360, 0), Point(510, 410, 0), Point(470, 410, 0), Point(470, 460, 0), Point(440, 460, 0)], Color(200, 0, 0, 255), Vector2(0.5, 0.5)),
        Slope([Point(540, 360, 0), Point(510, 360, 0), Point(510, 410, 0), Point(470, 410, 0), Point(470, 460, 0), Point(540, 460, 0)], Color(200, 0, 0, 255), Vector2(-0.5, -0.5)),
        Green([Point(440, 460, 0), Point(440, 530, 0), Point(410, 530, 0), Point(410, 680, 0), Point(570, 680, 0), Point(570, 530, 0), Point(540, 530, 0), Point(540, 460, 0)]),
        Sand([Point(410, 680, 0), Point(410, 720, 0), Point(610, 720, 0), Point(610, 530, 0), Point(570, 530, 0), Point(570, 680, 0)]),
        Water([Point(410, 720, 0), Point(410, 860, 0), Point(750, 860, 0), Point(750, 530, 0), Point(610, 530, 0), Point(610, 720, 0)]),
        Green([Point(540, 260, 0), Point(610, 90, 0), Point(370, 90, 0), Point(440, 260, 0)]),
        Rough([Point(610, 90, 0), Point(580, 170, 0), Point(690, 170, 0), Point(690, 90, 0)]),
        Green([Point(440, 90, 0), Point(440, 20, 0), Point(540, 20, 0), Point(540, 90, 0)]),
        Slope([Point(370, 90, 0), Point(410, 180, 0), Point(320, 230, 0), Point(270, 140, 0)], Color(200, 0, 0, 255), Vector2(-0.4, 0.25)),
        Green([Point(270, 140, 0), Point(120, 220, 0), Point(170, 310, 0), Point(320, 230, 0)]),
        Rough([Point(170, 310, 0), Point(120, 220, 0), Point(90, 400, 0)]),
        Green([Point(360, 610, 0), Point(120, 610, 0), Point(120, 640, 0), Point(400, 640, 0)]),
        Slope([Point(120, 640, 0), Point(120, 670, 0), Point(410, 670, 0), Point(410, 650, 0), Point(400, 640, 0)], Color(200, 0, 0, 255), Vector2(-0.1, 0.25)),
        Rough([Point(120, 580, 0), Point(30, 580, 0), Point(30, 670, 0), Point(120, 670, 0)]),
        Lava([Point(410, 720, 0), Point(410, 670, 0), Point(30, 670, 0), Point(30, 720, 0)]),
        Lava([Point(30, 580, 0), Point(30, 530, 0), Point(250, 530, 0), Point(320, 580, 0)]),
        Rough([Point(170, 310, 0), Point(250, 270, 0), Point(250, 380, 0)]),
        Water([Point(250, 270, 0), Point(410, 180, 0), Point(440, 260, 0), Point(440, 530, 0), Point(410, 530, 0), Point(250, 380, 0)]),
        Green([Point(410, 650, 0), Point(360, 610, 0), Point(320, 610, 0), Point(320, 580, 0), Point(90, 400, 0), Point(170, 310, 0), Point(410, 530, 0)]),
        Slope([Point(320, 610, 0), Point(320, 580, 0), Point(120, 580, 0), Point(120, 610, 0)], Color(200, 0, 0, 255), Vector2(-0.1, -0.25)),
        Pin(Point(495, 610, 0)),
        Tunnel(Point(490, 60, 0), Point(70, 630, 0), Vector2(1.0, 0.75)),
        Paywall(Point(440, 360, 0), Point(540, 360, 0), width=5, price=1),
        Paywall(Point(440, 460, 0), Point(540, 460, 0), width=5, price=1),
        Money(Point(487, 405, 0), amount=1),
        Wall(Point(540, 360, 0), Point(540, 460, 0), 5),
        Wall(Point(440, 360, 0), Point(440, 460, 0), 5),
        Wall(Point(440, 360, 0), Point(440, 260, 0), 5),
        Wall(Point(540, 360, 0), Point(540, 260, 0), 5),
        Wall(Point(540, 460, 0), Point(540, 530, 0), 5),
        Wall(Point(540, 530, 0), Point(750, 530, 0), 5),
        Wall(Point(750, 530, 0), Point(750, 860, 0), 5),
        Wall(Point(750, 860, 0), Point(410, 860, 0), 5),
        Wall(Point(440, 460, 0), Point(440, 530, 0), 5),
        Wall(Point(440, 530, 0), Point(410, 530, 0), 5),
        Wall(Point(540, 260, 0), Point(580, 170, 0), 5),
        Wall(Point(580, 170, 0), Point(690, 170, 0), 5),
        Wall(Point(690, 170, 0), Point(690, 90, 0), 5),
        Money(Point(640, 120, 0), amount=1),
        Wall(Point(690, 90, 0), Point(540, 90, 0), 5),
        Wall(Point(540, 90, 0), Point(540, 20, 0), 5),
        Wall(Point(540, 20, 0), Point(440, 20, 0), 5),
        Wall(Point(440, 20, 0), Point(440, 90, 0), 5),
        Wall(Point(440, 90, 0), Point(370, 90, 0), 5),
        Wall(Point(370, 90, 0), Point(120, 220, 0), 5),
        Wall(Point(120, 220, 0), Point(90, 400, 0), 5),
        Wall(Point(410, 180, 0), Point(440, 260, 0), 5),
        Wall(Point(250, 530, 0), Point(30, 530, 0), 5),
        Wall(Point(30, 530, 0), Point(30, 720, 0), 5),
        Wall(Point(30, 720, 0), Point(410, 720, 0), 5),
        Wall(Point(410, 720, 0), Point(410, 860, 0), 5),
        Wall(Point(90, 400, 0), Point(320, 580, 0), 5),
        Paywall(Point(320, 580, 0), Point(380, 500, 0), width=5, price=1),
        Wall(Point(380, 500, 0), Point(410, 530, 0), 5),
        Wall(Point(410, 180, 0), Point(320, 230, 0), 5)
    )
)
