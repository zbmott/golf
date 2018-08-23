# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

from pygame import draw

from src import constants
from src.utils import colors
from .Wall import Wall


class Paywall(Wall):
    def __init__(self, point1, point2, width=5, price=1, *groups):
        super().__init__(point1, point2, width=width, *groups)
        self.price = price

    def __repr__(self):
        msg = "{self.__class__.__name__}({p1!r}, {p2!r}, width={self.width!r}, price={self.price!r})"
        return msg.format(
            self=self,
            p1=self.point1 + self.origin,
            p2=self.point2 + self.origin
        )

    def update(self):
        super().update()
        draw.line(
            self.image,
            colors.GOLD,
            (self.point1.x, self.point1.y),
            (self.point2.x, self.point2.y),
            max(1, self.width // 3)
        )

    def handle_collision(self, ball):
        if self.price <= ball.funds:
            ball.funds -= self.price

            try:
                ball.velocity.scale_to_length(
                    ball.velocity.length() * constants.PAYWALL_COEFFICIENT
                )
            except ValueError:
                pass

            return self.kill()

        super().handle_collision(ball)
