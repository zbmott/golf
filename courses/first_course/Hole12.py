
from pygame import Color, font
from pygame.math import Vector2
from pygame.sprite import LayeredDirty

from src.models import Hole as BaseHole
from src.sprites import *
from src.utils import colors, Point


Hole = BaseHole(
    'Hole #11',
    par=3,
    origin=Point(75, 50, 0),
    ball=Point(180, 680, 0),
    noncollidibles=LayeredDirty(
        Text(Point(900, 75), 'Par 3', font.Font(None, 30), colors.WHITE),
    ),
    collidibles=LayeredDirty(
        Green([Point(130, 620, 0), Point(230, 620, 0), Point(230, 730, 0), Point(130, 730, 0)]),
        Rough([Point(230, 730, 0), Point(230, 680, 0), Point(350, 680, 0), Point(350, 730, 0)]),
        Slope([Point(230, 620, 0), Point(230, 540, 0), Point(350, 540, 0), Point(350, 620, 0)], Color(200, 0, 0, 255), Vector2(0.15, 0.4)),
        Green([Point(230, 620, 0), Point(230, 680, 0), Point(350, 680, 0), Point(350, 620, 0)]),
        Rough([Point(350, 460, 0), Point(470, 460, 0), Point(470, 730, 0), Point(350, 730, 0)]),
        Green([Point(470, 620, 0), Point(710, 620, 0), Point(710, 680, 0), Point(590, 680, 0), Point(590, 730, 0), Point(470, 730, 0)]),
        Green([Point(650, 620, 0), Point(650, 310, 0), Point(790, 310, 0), Point(790, 620, 0)]),
        Sand([Point(790, 620, 0), Point(790, 560, 0), Point(880, 560, 0), Point(880, 620, 0)]),
        Water([Point(790, 560, 0), Point(790, 450, 0), Point(880, 450, 0), Point(880, 560, 0)]),
        Sand([Point(790, 450, 0), Point(790, 310, 0), Point(880, 310, 0), Point(880, 450, 0)]),
        Slope([Point(470, 510, 0), Point(470, 390, 0), Point(650, 390, 0), Point(650, 510, 0)], Color(200, 0, 0, 255), Vector2(-0.2, -0.15)),
        Green([Point(470, 460, 0), Point(130, 460, 0), Point(130, 310, 0), Point(470, 310, 0)]),
        Rough([Point(470, 390, 0), Point(470, 190, 0), Point(560, 190, 0), Point(560, 390, 0)]),
        Water([Point(560, 390, 0), Point(560, 350, 0), Point(650, 350, 0), Point(650, 390, 0)]),
        Slope([Point(650, 350, 0), Point(650, 310, 0), Point(720, 310, 0), Point(720, 230, 0), Point(560, 230, 0), Point(560, 350, 0)], Color(200, 0, 0, 255), Vector2(-0.25, 0.45)),
        Sand([Point(130, 310, 0), Point(130, 230, 0), Point(290, 230, 0), Point(290, 310, 0)]),
        Slope([Point(470, 310, 0), Point(470, 230, 0), Point(290, 230, 0), Point(290, 310, 0)], Color(200, 0, 0, 255), Vector2(0.2, 0.0)),
        Green([Point(130, 230, 0), Point(130, 130, 0), Point(290, 130, 0), Point(290, 230, 0)]),
        Lava([Point(290, 180, 0), Point(360, 180, 0), Point(360, 30, 0), Point(130, 30, 0), Point(130, 130, 0), Point(290, 130, 0)]),
        Rough([Point(470, 190, 0), Point(470, 30, 0), Point(360, 30, 0), Point(360, 180, 0), Point(290, 180, 0), Point(290, 230, 0), Point(470, 230, 0)]),
        Green([Point(560, 190, 0), Point(560, 30, 0), Point(470, 30, 0), Point(470, 190, 0)]),
        Water([Point(560, 230, 0), Point(590, 230, 0), Point(590, 30, 0), Point(560, 30, 0)]),
        Green([Point(590, 60, 0), Point(770, 60, 0), Point(770, 30, 0), Point(880, 30, 0), Point(880, 150, 0), Point(770, 150, 0), Point(770, 110, 0), Point(590, 110, 0)]),
        Lava([Point(770, 60, 0), Point(770, 30, 0), Point(590, 30, 0), Point(590, 60, 0)]),
        Rough([Point(720, 230, 0), Point(720, 110, 0), Point(770, 110, 0), Point(770, 150, 0), Point(880, 150, 0), Point(880, 310, 0), Point(720, 310, 0)]),
        Sand([Point(590, 110, 0), Point(720, 230, 0), Point(720, 110, 0)]),
        Green([Point(590, 230, 0), Point(590, 110, 0), Point(720, 230, 0)]),
        Lava([Point(470, 590, 0), Point(580, 590, 0), Point(580, 540, 0), Point(650, 540, 0), Point(650, 510, 0), Point(470, 510, 0)]),
        Sand([Point(470, 590, 0), Point(470, 620, 0), Point(650, 620, 0), Point(650, 540, 0), Point(580, 540, 0), Point(580, 590, 0)]),
        Water([Point(130, 460, 0), Point(350, 460, 0), Point(350, 540, 0), Point(230, 540, 0), Point(230, 620, 0), Point(130, 620, 0)]),
        Rough([Point(790, 730, 0), Point(790, 650, 0), Point(880, 650, 0), Point(880, 730, 0)]),
        Slope([Point(880, 650, 0), Point(710, 650, 0), Point(710, 620, 0), Point(880, 620, 0)], Color(200, 0, 0, 255), Vector2(0.2, 0.25)),
        Slope([Point(790, 650, 0), Point(710, 650, 0), Point(710, 680, 0), Point(590, 680, 0), Point(590, 730, 0), Point(790, 730, 0), Point(790, 650, 0)], Color(200, 0, 0, 255), Vector2(-0.15, 0.0)),
        Pin(Point(830, 85, 0)),
        Tunnel(Point(180, 580, 0), Point(170, 380, 0), Vector2(2.5, -1.0)),
        Tunnel(Point(210, 180, 0), Point(560, 80, 0), Vector2(-1.25, 2.0)),
        Tunnel(Point(830, 690, 0), Point(610, 80, 0), Vector2(1.0, 1.5)),
        Wall(Point(130, 30, 0), Point(130, 730, 0), 5),
        Wall(Point(130, 730, 0), Point(880, 730, 0), 5),
        Wall(Point(880, 730, 0), Point(880, 30, 0), 5),
        Wall(Point(880, 30, 0), Point(130, 30, 0), 5),
        Money(Point(510, 290)),
    )
)
