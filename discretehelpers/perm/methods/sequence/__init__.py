from discretehelpers.a import true_except, have

from discretehelpers.perm.ex import LengthTooSmallError


def sequence(self, length=None):
    if have(length):
        true_except(length >= self.length, LengthTooSmallError)
    else:
        length = self.length
    return [self[i] for i in range(length)]
