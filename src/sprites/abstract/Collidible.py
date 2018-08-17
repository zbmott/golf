# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

import math, pygame


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

    def backup(self, other):
        """
        Back the other object up along whatever vector it was traveling
        until it is no longer in contact with this object.

        Return the vector used to back the ball up.
        """
        try:
            backup_vector = other.velocity.normalize()
            # ValueError is raised when ball.velocity has 0 magnitude.
        except ValueError:
            return

        while self.is_colliding_with(other):
            self.backup_step(backup_vector, other)

        return backup_vector

    def backup_step(self, backup_vector, other):
        """
        Scoot the ball one step backwards along its the given vector.
        """
        new_pos = other.logical_position - backup_vector
        other.set_logical_pos(new_pos)
        other.rect.x = math.ceil(new_pos.x)
        other.rect.y = math.ceil(new_pos.y)
