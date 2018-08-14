# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

from src.models import Course

from .Hole1 import Hole1
from .Hole2 import Hole2

__all__ = ['course']


course = Course('The First Course', [
    Hole1,
    Hole2,
])
