from os import path

from pygame import image, math
from pygame.sprite import DirtySprite

from src.utils import Point


class GolfBall(DirtySprite):
    RADIUS = 10
    GOLFBALL_PATH = path.join(
        path.dirname(path.dirname(path.dirname(__file__))),
        'assets',
        'golfball_20x20.png'
    )
    MAX_SPEED = 12
    MAX_SPEED_SQUARED = MAX_SPEED**2
    STRIKE_SCALE_FACTOR = 8

    def __init__(self, x, y, *groups):
        super().__init__(*groups)

        self.velocity = math.Vector2(0, 0)

        self.image = image.load(self.GOLFBALL_PATH)
        self.image.convert_alpha()

        self.rect = self.image.get_rect()
        self.logical_position = Point(x - self.RADIUS, y - self.RADIUS)
        
        self.rect.x = self.logical_position.x
        self.rect.y = self.logical_position.y

        self.in_contact_with_wall = False

    @property
    def center(self):
        return Point(
            int(self.logical_position.x + (self.rect.width / 2.0)),
            int(self.logical_position.y + (self.rect.height / 2.0))
        )

    def update(self):
        self.logical_position.x += self.velocity.x
        self.logical_position.y += self.velocity.y

        self.set_pos(int(self.logical_position.x), int(self.logical_position.y))

        self.dirty = 1

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def strike(self, x, y):
        self.velocity = math.Vector2(
            (self.center.x - x) / self.STRIKE_SCALE_FACTOR,
            (self.center.y - y) / self.STRIKE_SCALE_FACTOR
        )

        if self.velocity.length_squared() >= self.MAX_SPEED_SQUARED:
            self.velocity.scale_to_length(self.MAX_SPEED)

    def stop(self):
        self.velocity.x = 0
        self.velocity.y = 0

    def collidewall(self, walls):
        collisions = []
        initial_contact_state = self.in_contact_with_wall

        for wall in walls.sprites():
            if self.rect.collidelist(wall.rects) != -1:
                self.in_contact_with_wall = True
                collisions.append(wall)

        if not initial_contact_state and collisions:
            return collisions

        self.in_contact_with_wall = False
        return []
