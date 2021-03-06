# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

import pygame
from pygame import draw, math, mouse, Surface
from pygame.sprite import LayeredDirty

from src import constants
from src.sprites import GolfBall
from src.utils import colors, Point


class Hole(object):
    def __init__(self, name='untitled', par=3, origin=Point(50, 50), width=1080, height=900, ball=None, **labeled_groups):
        self.score = -1
        self.name = name
        self.par = par
        self.origin = origin
        self.width = width
        self.height = height

        self.image = Surface((width, height))

        self.rect = pygame.Rect(*origin.as_2d_tuple(), width, height)

        self.groups = {'all': LayeredDirty()}

        for label, group in labeled_groups.items():
            self.groups[label] = group
            self.groups['all'].add(*group.sprites())

        self.ball = GolfBall(ball, 0, self.groups['all']) if ball else None

    def update(self):
        self.groups['all'].update()

        for c in self.groups['collidibles']:
            c.collide_with(self.ball)

    def draw(self, show_pointer=True, show_velocity=True):
        self.image.fill(colors.DARKGRAY)
        self.groups['all'].draw(self.image)

        if show_velocity and self.ball.velocity:
            self._visualize_velocity(self.ball, self.image)

        if show_pointer and self.ball.velocity.length_squared() == 0:
            self._draw_pointer(self.ball, self.image)

        return self.image

    def handle_event(self, e):
        if e.type in [pygame.MOUSEBUTTONDOWN]:
            if e.button == 1:
                self.ball.strike(e.pos[0] - self.origin.x, e.pos[1] - self.origin.y)
                self.score += 1
        if e.type in [pygame.USEREVENT]:
            if e.code == 'penalty':
                self.score += e.degree

    def _visualize_velocity(self, ball, surface):
        """
        Draw a line that visualizes ball's current velocity.
        """
        draw.line(
            surface,
            (255, 0, 0),
            (ball.center.x, ball.center.y),
            (ball.center.x + int(constants.STRIKE_SCALE_FACTOR * ball.velocity.x),
             ball.center.y + int(constants.STRIKE_SCALE_FACTOR * ball.velocity.y)),
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

        max_speed = constants.MAX_SPEED * constants.STRIKE_SCALE_FACTOR

        if mouse_vec.length_squared() > max_speed ** 2:
            mouse_vec.scale_to_length(max_speed)

        draw.line(
            surface,
            (0, 0, 255),
            (ball.center.x, ball.center.y),
            (int(ball.center.x - mouse_vec.x),
             int(ball.center.y - mouse_vec.y)),
            3
        )

        power = int(mouse_vec.length() / max_speed * 100)
        font = pygame.font.Font(None, 20)

        surface.blit(
            font.render("{power!s}%".format(power=power), True, colors.WHITE),
            (ball.center.x + 10, ball.center.y + 10)
        )

