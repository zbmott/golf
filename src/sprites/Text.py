# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

from pygame import Rect
from pygame.sprite import DirtySprite


class Text(DirtySprite):
    def __init__(self, point, text, font, color, *groups):
        super().__init__(*groups)

        self.point = point

        self.image = font.render(text, True, color)
        self.rect = Rect(
            point.x, point.y,
            self.image.get_width(),
            self.image.get_height()
        )
