# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'


from pygame import draw, math, Rect, sprite, Surface
from pygame.sprite import DirtySprite

from src.utils import Point
from .Collidible import Collidible


class Wall(DirtySprite, Collidible):
    WALL_COLOR = (102, 51, 0)  # Brown.

    def __init__(self, point1, point2, width, *groups):
        super().__init__(*groups)

        self.width = width

        # This sprite's origin on the application's screen.
        # Necessary to draw the sprite correctly, as well as to calculate
        # collision rectangles correctly.
        self.origin = Point(min(point1.x, point2.x), min(point1.y, point2.y))

        self.point1 = point1 - self.origin
        self.point2 = point2 - self.origin

        self._draw_vector = math.Vector2(*(self.point2 - self.point1).as_2d_tuple())
        self._draw_vector.scale_to_length(1)
        self.reflect_vector = math.Vector2(self._draw_vector.y, self._draw_vector.x)

        self.image = Surface((
            abs(point2.x - point1.x) + self.width,
            abs(point2.y - point1.y) + self.width
        ))
        self.image.set_colorkey((0, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.x = self.origin.x
        self.rect.y = self.origin.y

        self.collision_rects = self.calculate_rectangles()

    def calculate_rectangles(self):
        rects = []
        current_pixel = self.point1
        real_pixel = Point(int(current_pixel.x), int(current_pixel.y))

        while real_pixel != self.point2:
            rects.append(Rect(
                *(current_pixel + self.origin).as_2d_tuple(),
                self.width,
                self.width
            ))

            current_pixel += self._draw_vector
            real_pixel = Point(int(current_pixel.x), int(current_pixel.y))

        return rects

    def update(self):
        draw.line(
            self.image,
            self.WALL_COLOR,
            (self.point1.x, self.point1.y),
            (self.point2.x, self.point2.y),
            self.width
        )

    def handle_collision(self, ball):
        ball.velocity.reflect_ip(self.reflect_vector)
