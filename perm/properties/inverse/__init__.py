from a import have


@property
def inverse(self):
    return self._inverse


@inverse.setter
def inverse(self, val):
    self._inverse = val


@inverse.getter
def inverse(self):

    if have(self._inverse):
        return self._inverse

    from perm import Perm

    inverse_map = dict((self.mapping[key], key) for key in self.mapping.keys())
    result = Perm(inverse_map)

    self.inverse = result
    return result
