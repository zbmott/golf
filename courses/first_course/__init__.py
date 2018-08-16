# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

from src.models import Course

__all__ = ['course']


course = Course('The First Course', [
    'courses.first_course.Hole1',
    'courses.first_course.Hole2',
    'courses.first_course.Hole3',
    'courses.first_course.Hole4',
])
