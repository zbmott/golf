# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'


class Course(object):
    """
    Container for a set of holes. Pretty dumb right now, but may grow
    in the future.
    """
    def __init__(self, name, holes):
        self.name = name
        self.holes = holes

    @property
    def total_par(self):
        return sum([h.par for h in self.holes])
