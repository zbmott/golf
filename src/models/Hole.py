# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'

from pygame.sprite import RenderUpdates


class Hole(object):
    """
    """
    def __init__(self, name, par, **labeled_groups):
        self.name = name
        self.par = par

        self.groups = {'all': RenderUpdates()}

        for label, group in labeled_groups.items():
            self.groups[label] = group
            self.groups['all'].add(*group.sprites())
