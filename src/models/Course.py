# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'


class Course(object):
    """
    Container for a set of holes. Pretty dumb right now, but may grow
    in the future.
    """
    def __init__(self, name, holes):
        self.name = name
        self.holes = iter(holes)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.holes)
