from discretehelpers.a import have


@property
def parity(self):
    return self._parity


@parity.setter
def parity(self, val):
    self._parity = val


@parity.getter
def parity(self):

    if have(self._parity):
        return self._parity

    result = len(self.inversion_set) % 2

    self.parity = result
    return result
