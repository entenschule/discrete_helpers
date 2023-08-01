from discretehelpers.a import have


def slice_to_range(s, stop=None):

    start = s.start if have(s.start) else 0
    stop = s.stop if have(s.stop) else stop
    step = s.step if have(s.step) else 1

    assert have(stop)

    return range(start, stop, step)
