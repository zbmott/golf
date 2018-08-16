# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'


from os import path

import pygame
from pygame import event, Rect

from src import constants
from src.utils import Point
from .abstract import Collidible
from .ImageSprite import ImageSprite


class Pin(ImageSprite, Collidible):
    IMAGE_PATH = path.join(
        path.dirname(path.dirname(path.dirname(__file__))),
        'assets',
        'pin_25x25.png',
    )

    def __init__(self, point, *groups):
        super().__init__(*groups)

        self._layer = constants.LAYER_PIN

        self.rect.x = point.x
        self.rect.y = point.y

        self.collision_rects = [
            Rect(
                self.rect.x + (self.rect.width / 2),
                self.rect.y + (self.rect.height / 2),
                1,
                1
            )
        ]

    def __repr__(self):
        return "Pin({p!r})".format(p=Point(self.rect.x, self.rect.y))

    @property
    def center(self):
        return Point(self.collision_rects[0].x, self.collision_rects[0].y)

    def collide_with(self, ball):
        # If the ball is overlapping any portion of the hole,
        # give it a little push into the cup.
        if self.is_colliding_with(ball):
            if ball.velocity.length_squared() >= 0.5:
                center = self.center
                push = pygame.math.Vector2(
                    center.x - ball.center.x,
                    center.y - ball.center.y
                )
                push.scale_to_length(0.2)
                ball.velocity += push

        # If the ball is overlapping the center of the pin, see if
        # the player sank the putt.
        if ball.collision_rect.collidepoint(self.center.as_2d_tuple()):
            self.sink_putt(ball)

    def sink_putt(self, ball):
        if ball.velocity.length_squared() <= constants.SINK_THRESHOLD:
            ball.stop()
            ball.center_on(self.center)

            event.post(event.Event(pygame.USEREVENT, code='hole_complete'))
