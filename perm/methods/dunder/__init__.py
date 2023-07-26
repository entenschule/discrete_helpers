from a import true_except, is_natural, slice_to_range

from perm.ex import OtherNotPermError


def __getitem__(self, arg):
    if is_natural(arg):
        if self.neutral:
            return arg
        if arg in self.moved:
            return self.mapping[arg]
        else:
            return arg
    elif isinstance(arg, slice):
        return [self[i] for i in slice_to_range(arg, self.length)]
    else:
        raise ValueError


def __eq__(self, other):
    from perm import Perm
    true_except(isinstance(other, Perm), OtherNotPermError)
    if self.neutral and other.neutral:
        return True
    else:
        return self.mapping == other.mapping


def __str__(self):
    if self.neutral:
        return 'Perm()'
    string = str(list(self.cycles))
    return f'Perm({string})'


def __repr__(self):
    return self.__str__()


def __hash__(self):
    return hash(self.__str__())


def __mul__(self, other):  # a * b means a after b (function composition)
    from perm import Perm
    true_except(isinstance(other, Perm), OtherNotPermError)
    if self.neutral:
        return other
    if other.neutral:
        return self

    moved = self.moved.union(other.moved)
    mapping = dict()
    for i in moved:
        mapping[i] = self[other[i]]
    return Perm(mapping)


def __pow__(self, exponent):
    if exponent == 0:
        from perm import Perm
        return Perm()
    if exponent == 1:
        return self
    if exponent == -1:
        return self.inverse

    if exponent > 1:
        result = self
        for i in range(exponent - 1):
            result *= self
        return result
    elif exponent < -1:
        inverse = self.inverse
        result = inverse
        for i in range(-exponent - 1):
            result *= inverse
        return result
