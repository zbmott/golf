# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

import pygame

from src.utils import colors
from .abstract import FrictionalSurface


class Lava(FrictionalSurface):
    def __init__(self, points, *groups):
        super().__init__(points, colors.LAVA, 0.7, *groups)

    def handle_collision(self, ball):
        super().handle_collision(ball)

        if not ball.should_collide_with_surface:  # I.e. the ball isn't moving.
            pygame.event.post(pygame.event.Event(
                pygame.USEREVENT,
                code='die',
                message='You fell into the lava and died.'
            ))
