# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

import pygame


class Collidible(object):
    """
    Quick note on orthography: as of 2018-08-14, "collidible" has an order of
    magnitude more hits on Google than "collidable", which is why I chose it.
    """
    def is_colliding_with(self, other):
        return pygame.sprite.collide_mask(self, other)

    def handle_collision(self, other):
        raise NotImplementedError()

    def collide_with(self, other):
        """
        Act on 'other' only if it is colliding with this object.
        """
        if not self.is_colliding_with(other):
            return

        self.handle_collision(other)
