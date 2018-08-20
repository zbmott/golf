
from pygame import Color, font
from pygame.math import Vector2
from pygame.sprite import LayeredDirty

from src.models import Hole as BaseHole
from src.sprites import *
from src.utils import colors, Point


Hole = BaseHole(
    'Hole #9',
    par=3,
    origin=Point(150, 50, 0),
    ball=Point(505, 450, 0),
    noncollidibles=LayeredDirty(
        Text(Point(590, 143), 'Par 3', font.Font(None, 30), colors.WHITE),
    ),
    collidibles=LayeredDirty(
        Green([Point(450, 100, 0), Point(560, 100, 0), Point(560, 200, 0), Point(450, 200, 0)]),
        Lava([Point(450, 200, 0), Point(440, 200, 0), Point(440, 90, 0), Point(450, 90, 0)]),
        Lava([Point(450, 100, 0), Point(450, 90, 0), Point(570, 90, 0), Point(570, 100, 0)]),
        Lava([Point(560, 100, 0), Point(560, 210, 0), Point(570, 210, 0), Point(570, 100, 0)]),
        Lava([Point(560, 210, 0), Point(440, 210, 0), Point(440, 200, 0), Point(560, 200, 0)]),
        Green([Point(440, 210, 0), Point(440, 510, 0), Point(570, 510, 0), Point(570, 210, 0)]),
        Slope([Point(570, 510, 0), Point(570, 360, 0), Point(620, 360, 0), Point(620, 510, 0)], Color(200, 0, 0, 255), Vector2(0.33, 0.0)),
        Green([Point(620, 360, 0), Point(750, 510, 0), Point(620, 510, 0)]),
        Slope([Point(620, 510, 0), Point(620, 560, 0), Point(750, 560, 0), Point(750, 510, 0)], Color(200, 0, 0, 255), Vector2(0.0, 0.4)),
        Green([Point(620, 560, 0), Point(620, 700, 0), Point(750, 560, 0)]),
        Slope([Point(620, 560, 0), Point(570, 560, 0), Point(570, 700, 0), Point(620, 700, 0)], Color(200, 0, 0, 255), Vector2(-0.5, 0.0)),
        Green([Point(340, 560, 0), Point(340, 620, 0), Point(570, 620, 0), Point(570, 560, 0)]),
        Rough([Point(570, 700, 0), Point(570, 620, 0), Point(340, 620, 0), Point(340, 700, 0)]),
        Slope([Point(340, 560, 0), Point(290, 560, 0), Point(290, 700, 0), Point(340, 700, 0)], Color(200, 0, 0, 255), Vector2(-0.55, 0.0)),
        Green([Point(290, 560, 0), Point(160, 560, 0), Point(290, 700, 0)]),
        Sand([Point(160, 560, 0), Point(160, 530, 0), Point(290, 530, 0), Point(290, 560, 0)]),
        Green([Point(160, 530, 0), Point(160, 430, 0), Point(290, 430, 0), Point(290, 530, 0)]),
        Sand([Point(160, 430, 0), Point(160, 400, 0), Point(290, 400, 0), Point(290, 430, 0)]),
        Green([Point(160, 400, 0), Point(160, 300, 0), Point(290, 300, 0), Point(290, 400, 0)]),
        Sand([Point(160, 300, 0), Point(160, 270, 0), Point(290, 270, 0), Point(290, 300, 0)]),
        Green([Point(160, 270, 0), Point(160, 140, 0), Point(290, 140, 0), Point(290, 270, 0)]),
        Water([Point(160, 560, 0), Point(60, 560, 0), Point(60, 40, 0), Point(160, 40, 0)]),
        Water([Point(160, 40, 0), Point(440, 40, 0), Point(440, 510, 0), Point(620, 510, 0), Point(620, 560, 0), Point(290, 560, 0), Point(290, 140, 0), Point(160, 140, 0)]),
        Pin(Point(505, 150, 0)),
        Pin(Point(225, 200, 0)),
        Wall(Point(160, 560, 0), Point(60, 560, 0), 5),
        Wall(Point(60, 560, 0), Point(60, 40, 0), 5),
        Wall(Point(60, 40, 0), Point(440, 40, 0), 5),
        Wall(Point(440, 40, 0), Point(440, 90, 0), 5),
        Wall(Point(440, 90, 0), Point(570, 90, 0), 5),
        Wall(Point(570, 90, 0), Point(570, 360, 0), 5),
        Wall(Point(570, 360, 0), Point(620, 360, 0), 5),
        Wall(Point(620, 360, 0), Point(750, 510, 0), 5),
        Wall(Point(750, 510, 0), Point(750, 560, 0), 5),
        Wall(Point(750, 560, 0), Point(620, 700, 0), 5),
        Wall(Point(620, 700, 0), Point(290, 700, 0), 5),
        Wall(Point(290, 700, 0), Point(160, 560, 0), 5)
    )
)
