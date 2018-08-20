# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

import pygame

from src.utils import colors
from .abstract import FrictionalSurface


class Water(FrictionalSurface):
    def __init__(self, points, *groups):
        super().__init__(points, colors.BLUE, 0.8, *groups)

    # def is_colliding_with(self, ball):
    #     return self.rect.colliderect(pygame.Rect(
    #         ball.center.x - 5,
    #         ball.center.y - 5,
    #         10, 10
    #     ))

    def handle_collision(self, ball):
        """
        The ball collides with Water like a normal frictional surface, but
        there's extra logic for what happens if the ball comes to a stop
        while in contact with Water.
        """
        super().handle_collision(ball)

        # If the ball stopped in the water, back it up along its previous
        # velocity vector until it's no longer in contact with the water,
        # then charge the player an additional stroke.
        if not ball.should_collide_with_surface:
            ball.velocity = ball.previous_velocities[-1]

            vec = self.backup(ball)
            for _ in range(5):
                self.backup_step(vec, ball)

            ball.stop()

            pygame.event.post(pygame.event.Event(
                pygame.USEREVENT,
                code='penalty',
                degree=1
            ))
