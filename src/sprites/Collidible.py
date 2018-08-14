# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@nerdery.com'


class Collidible(object):
    """
    Quick note on orthography: as of 2018-08-14, "collidible" has an order of
    magnitude more hits on Google than "collidable", which is why I chose it.
    """
    def __init__(self):
        super().__init__()
        self.collision_rects = []

    def handle_collision(self, other):
        raise NotImplementedError()
