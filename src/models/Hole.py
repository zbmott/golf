# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

import pygame
from pygame import draw, math, mouse, Surface
from pygame.sprite import RenderUpdates

from src.utils import colors, Point


class Hole(object):
    """
    """
    def __init__(self, name, par, origin, width=1080, height=800, **labeled_groups):
        self.score = -1
        self.name = name
        self.par = par
        self.origin = origin
        self.width = width
        self.height = height

        self.image = Surface((width, height))

        self.groups = {'all': RenderUpdates()}

        for label, group in labeled_groups.items():
            self.groups[label] = group
            self.groups['all'].add(*group.sprites())

        self.ball = self.groups['ball'].sprites()[0]

    def update(self):
        collisions = self.ball.collide(self.groups['collidibles'])
        for collision in collisions:
            collision.handle_collision(self.ball)

        self.groups['all'].update()

    def draw(self):
        self.image.fill(colors.DARKGRAY)
        self.groups['all'].draw(self.image)

        if self.ball.velocity:
            self._visualize_velocity(self.ball, self.image)

        if self.ball.velocity.length_squared() == 0:
            self._draw_pointer(self.ball, self.image)

        return self.image

    def handle_event(self, e):
        if e.type in [pygame.MOUSEBUTTONDOWN]:
            if e.button == 1:
                self.ball.strike(e.pos[0] - self.origin.x, e.pos[1] - self.origin.y)
                self.score += 1

    def _visualize_velocity(self, ball, surface):
        """
        Draw a line that visualizes ball's current velocity.
        """
        draw.line(
            surface,
            (255, 0, 0),
            (ball.center.x, ball.center.y),
            (ball.center.x + int(ball.STRIKE_SCALE_FACTOR * ball.velocity.x),
             ball.center.y + int(ball.STRIKE_SCALE_FACTOR * ball.velocity.y)),
            3
        )

    def _draw_pointer(self, ball, surface):
        """
        Draw a line that visualizes strike direction and power.
        """
        mouse_pos = Point(*mouse.get_pos())
        mouse_vec = math.Vector2(
            mouse_pos.x - ball.center.x - self.origin.x,
            mouse_pos.y - ball.center.y - self.origin.y
        )

        if mouse_vec.length_squared() >= (ball.MAX_SPEED * ball.STRIKE_SCALE_FACTOR) ** 2:
            mouse_vec.scale_to_length(ball.MAX_SPEED * ball.STRIKE_SCALE_FACTOR)

        draw.line(
            surface,
            (0, 0, 255),
            (ball.center.x, ball.center.y),
            (int(ball.center.x - mouse_vec.x),
             int(ball.center.y - mouse_vec.y)),
            3
        )
