#!/usr/bin/env python

import sys
import pygame
from pygame.locals import Rect
from pygame import draw, math, mouse

from src.sprites import *
from src.utils import Point

DEFAULT_SCREEN = Rect(0, 0, 640, 480)


def main():
    pygame.init()

    clock = pygame.time.Clock()

    background = pygame.display.set_mode((640, 480), pygame.RESIZABLE)

    walls = pygame.sprite.Group()
    all = pygame.sprite.RenderUpdates()

    ball = GolfBall(320, 240, [all])
    Wall(Point(30, 30), Point(610, 45), 3, [all, walls])
    Wall(Point(610, 45), Point(595, 465), 3, [all, walls])
    Wall(Point(595, 465), Point(45, 450), 3, [all, walls])
    Wall(Point(45, 450), Point(30, 30), 3, [all, walls])

    while True:
        keystate = None
        screen = pygame.display.get_surface()

        # Check for interesting stuff.
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                return 0
            elif event.type in [pygame.VIDEORESIZE]:
                background = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            elif event.type in [pygame.MOUSEBUTTONDOWN]:
                if event.button == 1:
                    ball.strike(*event.pos)
            elif event.type in [pygame.KEYDOWN]:
                keystate = event.key

        if keystate == 115:  # 's'
            ball.stop()

        collisions = ball.collidewall(walls)
        for collision in collisions:
            ball.velocity.reflect_ip(collision.reflect_vector)

        all.clear(screen, background)
        screen.fill((0, 100, 0))
        all.update()

        # Visualize the ball's current velocity
        if ball.velocity:
            draw.line(
                screen,
                (255, 0, 0),
                (ball.center.x, ball.center.y),
                (ball.center.x + ball.STRIKE_SCALE_FACTOR*int(ball.velocity.x),
                 ball.center.y + ball.STRIKE_SCALE_FACTOR*int(ball.velocity.y)),
                3
            )

        # Draw line from mouse pointer to ball
        if ball.velocity.length_squared() == 0:
            mouse_pos = Point(*mouse.get_pos())
            mouse_vec = math.Vector2(
                mouse_pos.x - ball.center.x,
                mouse_pos.y - ball.center.y
            )

            if mouse_vec.length_squared() >= (ball.MAX_SPEED*ball.STRIKE_SCALE_FACTOR)**2:
                mouse_vec.scale_to_length(ball.MAX_SPEED * ball.STRIKE_SCALE_FACTOR)

            draw.line(
                screen,
                (0, 0, 255),
                (ball.center.x, ball.center.y),
                (int(ball.center.x - mouse_vec.x),
                 int(ball.center.y - mouse_vec.y)),
                3
            )

        dirty = all.draw(screen)
        pygame.display.update(dirty)

        clock.tick(33)  # Framerate capped at ~30 FPS


if __name__ == '__main__':
    sys.exit(main())
