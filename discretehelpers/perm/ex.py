class ArgTypeError(TypeError):
    """The first argument of `Perm` must be a list (of integers or lists) or a dict."""


class SequenceError(ValueError):
    """A sequence of length n must contain all integers from 0 to n-1."""


class CyclesError(ValueError):
    """The cycles must be lists of integers."""


class DictError(ValueError):
    """Keys and values of the dict must be from the same set of integers."""


class OtherNotPermError(TypeError):
    """If `a` is of type Perm, these expressions make only sense if `b` is as well: `a * b`, `a == b`"""


class LengthTooSmallError(ValueError):
    """When a finite permutation is represented as a sequence, its length must be greater than the moved elements."""
