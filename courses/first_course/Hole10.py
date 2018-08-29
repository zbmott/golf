
from pygame import Color, font
from pygame.math import Vector2
from pygame.sprite import LayeredDirty

from src.models import Hole as BaseHole
from src.sprites import *
from src.utils import colors, Point


Hole = BaseHole(
    'Hole #10',
    par=2,
    origin=Point(50, 75, 0),
    ball=Point(485, 690, 0),
    noncollidibles=LayeredDirty(
        Text(Point(810, 340), 'Par 2', font.Font(None, 30), colors.WHITE),
    ),
    collidibles=LayeredDirty(
        Rough([Point(300, 430, 0), Point(340, 430, 0), Point(340, 470, 0), Point(300, 470, 0)]),
        Rough([Point(630, 430, 0), Point(670, 430, 0), Point(670, 470, 0), Point(630, 470, 0)]),
        Slope([Point(300, 430, 0), Point(260, 390, 0), Point(380, 390, 0), Point(340, 430, 0)], Color(200, 0, 0, 255), Vector2(0.0, 0.1)),
        Slope([Point(380, 390, 0), Point(340, 430, 0), Point(340, 470, 0), Point(380, 510, 0)], Color(200, 0, 0, 255), Vector2(-0.1, 0.0)),
        Slope([Point(380, 510, 0), Point(340, 470, 0), Point(300, 470, 0), Point(260, 510, 0)], Color(200, 0, 0, 255), Vector2(0.0, -0.1)),
        Slope([Point(260, 510, 0), Point(300, 470, 0), Point(300, 430, 0), Point(260, 390, 0)], Color(200, 0, 0, 255), Vector2(0.1, 0.0)),
        Slope([Point(590, 390, 0), Point(630, 430, 0), Point(670, 430, 0), Point(710, 390, 0)], Color(200, 0, 0, 255), Vector2(0.0, -0.15)),
        Slope([Point(710, 390, 0), Point(670, 430, 0), Point(670, 470, 0), Point(710, 510, 0)], Color(200, 0, 0, 255), Vector2(0.15, 0.0)),
        Slope([Point(710, 510, 0), Point(670, 470, 0), Point(630, 470, 0), Point(590, 510, 0)], Color(200, 0, 0, 255), Vector2(0.0, 0.15)),
        Slope([Point(590, 510, 0), Point(630, 470, 0), Point(630, 430, 0), Point(590, 390, 0)], Color(200, 0, 0, 255), Vector2(-0.15, 0.0)),
        Green([Point(210, 340, 0), Point(760, 340, 0), Point(760, 390, 0), Point(210, 390, 0)]),
        Green([Point(260, 390, 0), Point(210, 390, 0), Point(210, 740, 0), Point(260, 740, 0)]),
        Green([Point(760, 390, 0), Point(760, 740, 0), Point(260, 740, 0), Point(260, 510, 0), Point(380, 510, 0), Point(380, 390, 0), Point(590, 390, 0), Point(590, 510, 0), Point(710, 510, 0), Point(710, 390, 0)]),

        Green([Point(160, 10, 0), Point(160, 310, 0), Point(310, 310, 0), Point(310, 10, 0)]),
        Slope([Point(310, 310, 0), Point(310, 110, 0), Point(360, 110, 0), Point(360, 210, 0), Point(410, 210, 0), Point(410, 310, 0)], Color(200, 0, 0, 255), Vector2(0.25, -0.5)),
        Slope([Point(310, 10, 0), Point(310, 110, 0), Point(360, 110, 0), Point(360, 210, 0), Point(410, 210, 0), Point(410, 10, 0)], Color(200, 0, 0, 255), Vector2(-0.35, 0.33)),
        Green([Point(410, 10, 0), Point(710, 10, 0), Point(710, 110, 0), Point(880, 110, 0), Point(880, 210, 0), Point(710, 210, 0), Point(710, 310, 0), Point(410, 310, 0)]),
        Sand([Point(880, 260, 0), Point(710, 260, 0), Point(710, 210, 0), Point(880, 210, 0), Point(880, 110, 0), Point(710, 110, 0), Point(710, 60, 0), Point(930, 60, 0), Point(930, 260, 0)]),
        Water([Point(710, 310, 0), Point(1030, 310, 0), Point(1030, 10, 0), Point(710, 10, 0), Point(710, 60, 0), Point(930, 60, 0), Point(930, 260, 0), Point(710, 260, 0)]),
        Pin(Point(828, 160, 0)),

        Tunnel(Point(320, 450, 0), Point(230, 280, 0), Vector2(-0.75, -2.0)),
        Tunnel(Point(650, 450, 0), Point(450, 290, 0), Vector2(-2.0, -0.75)),
        Money(Point(480, 440, 0), amount=1),
        Wall(Point(160, 10, 0), Point(1030, 10, 0), 5),
        Wall(Point(1030, 10, 0), Point(1030, 310, 0), 5),
        Wall(Point(1030, 310, 0), Point(160, 310, 0), 5),
        Wall(Point(160, 310, 0), Point(160, 10, 0), 5),

        Wall(Point(210, 340, 0), Point(760, 340, 0), 5),
        Wall(Point(760, 340, 0), Point(760, 740, 0), 5),
        Wall(Point(760, 740, 0), Point(210, 740, 0), 5),
        Wall(Point(210, 740, 0), Point(210, 340, 0), 5),
    )
)
