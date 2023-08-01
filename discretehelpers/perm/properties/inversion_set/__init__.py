from discretehelpers.a import have
from .work import work


@property
def inversion_set(self):
    return self._inversion_set


@inversion_set.setter
def inversion_set(self, val):
    self._inversion_set = val


@inversion_set.getter
def inversion_set(self):

    if have(self._inversion_set):
        return self._inversion_set

    result = work(self)

    self.inversion_set = result
    return result
