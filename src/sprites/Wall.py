# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'


from pygame import draw, mask, math, sprite, Surface
from pygame.sprite import DirtySprite

from src import constants
from src.utils import colors, Point
from .abstract import Collidible


class Wall(DirtySprite, Collidible):
    def __init__(self, point1, point2, width=5, *groups):
        super().__init__(*groups)

        self._layer = constants.LAYER_WALL

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
        self.image.set_colorkey(colors.BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = self.origin.x
        self.rect.y = self.origin.y

        self.update()
        self.mask = mask.from_surface(self.image)

    def __repr__(self):
        return "Wall({p1!r}, {p2!r}, {self.width!r})".format(
            p1=self.point1 + self.origin,
            p2=self.point2 + self.origin,
            self=self,
        )

    @classmethod
    def create_for_editor(cls, points):
        return cls(points[0], points[1])

    def update(self):
        draw.line(
            self.image,
            colors.BROWN,
            (self.point1.x, self.point1.y),
            (self.point2.x, self.point2.y),
            self.width
        )

    def handle_collision(self, ball):
        """
        When the ball hits a wall, we back it up along its velocity vector
        until it's no longer in contact with the wall, then we reflect its
        velocity vector along the wall's axis.
        """
        # If the ball is no longer actually in contact with this wall
        # (perhaps because a previous collision altered its position),
        # do nothing.
        if not sprite.collide_mask(self, ball):
            return

        try:
            backup_vector = ball.velocity.normalize()

        # ValueError is raised when ball.velocity has 0 magnitude.
        except ValueError:
            return

        while sprite.collide_mask(self, ball):
            new_pos = ball.logical_position - backup_vector
            ball.set_logical_pos(new_pos)
            ball.rect.x = new_pos.x
            ball.rect.y = new_pos.y

        ball.velocity.reflect_ip(self.reflect_vector)
        ball.velocity.scale_to_length(ball.velocity.length() * constants.WALL_ELASTICITY)
