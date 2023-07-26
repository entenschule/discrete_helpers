import numpy as np

from a import is_natural as f


def test():
    assert f(0)
    assert f(123)
    assert f(np.int64(123))
    assert f(False)
    assert f(True)

    assert not f('1')
    assert not f(1.5)
    assert not f(-1)

