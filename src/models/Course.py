# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

import pickle
from collections.abc import Iterable

from importlib import import_module

from .Hole import Hole


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

    @property
    def total_score(self):
        return sum([h.score for h in self.holes if h.score > -1])

    def load(self):
        resolved_holes = []

        for hole in self.holes:
            if isinstance(hole, Hole):
                resolved_holes.append(hole)
            if isinstance(hole, str):
                if hole.endswith('pkl'):
                    resolved_holes += self.load_pickle(hole)
                else:
                    resolved_holes.append(self.load_class(hole))

        self.holes = resolved_holes

    def load_pickle(self, hole):
        with open(hole, 'rb') as infile:
            contents = pickle.load(infile)

        if isinstance(contents, Hole):
            return [contents]
        elif isinstance(contents, Iterable):
            return contents

    def load_class(self, hole):
        return import_module(hole).Hole
