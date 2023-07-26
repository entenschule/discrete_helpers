import numpy as np
from a import have


@property
def order(self):
    return self._order


@order.setter
def order(self, val):
    self._order = val


@order.getter
def order(self):
    """lowest positive exponent that will produce the identity"""

    if have(self._order):
        return self._order

    if self.neutral:
        self.order = 1
        return 1

    cycle_lengths = [len(cycle) for cycle in self.cycles]
    result = np.lcm.reduce(cycle_lengths)

    self.order = result
    return result
