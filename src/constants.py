# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'


LAYER_GROUND = 0
LAYER_PIN = 5
LAYER_BALL = 10
LAYER_WALL = 15
LAYER_TEXT = 100

MAX_FPS = 60
MAX_SPEED = 20
MAX_SPEED_SQUARED = MAX_SPEED ** 2

PAYWALL_COEFFICIENT = 0.925
PIN_NUDGE_FACTOR = 0.2
PIN_NUDGE_THRESHOLD = 0.5

SINK_THRESHOLD = MAX_SPEED_SQUARED * 0.0275
STOPPING_THRESHOLD = 0.025
STRIKE_SCALE_FACTOR = 7.5

WALL_ELASTICITY = 0.8
