# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'


from pygame import image, mask
from pygame.sprite import DirtySprite


class ImageSprite(DirtySprite):
    IMAGE_PATH = NotImplemented

    def __init__(self, *groups):
        super().__init__(*groups)

        self.dirty = 2

        self.image = image.load(self.IMAGE_PATH)
        self.image.convert_alpha()

        self.mask = mask.from_surface(self.image)

        self.rect = self.image.get_rect()
