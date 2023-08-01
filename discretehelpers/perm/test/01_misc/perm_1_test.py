from discretehelpers.a import abbrev_testing as abbrev
from discretehelpers.perm import Perm
from discretehelpers.perm.ex import LengthTooSmallError


def test_init():

    # sequence
    a = Perm([3, 0, 1, 2, 6, 5, 4])
    b = Perm([3, 0, 1, 2, 6, 5, 4, 7, 8])

    # cycles
    c = Perm([[0, 3, 2, 1], [4, 6]])
    d = Perm([[0, 3, 2, 1], [4, 6], [5], [999]])
    e = Perm([[6, 4], [2, 1, 0, 3]])

    # mapping
    f = Perm({0: 3, 1: 0, 2: 1, 3: 2, 4: 6, 6: 4})
    g = Perm({0: 3, 1: 0, 2: 1, 3: 2, 4: 6, 6: 4, 99: 99})

    assert a == b == c == d == e == f == g


def test_neutral():

    a = Perm()
    b = Perm([[1], [3]])
    assert a.neutral and b.neutral
    assert a.sequence() == a.cycles == b.sequence() == b.cycles == list()
    assert a.mapping == b.mapping == dict()
    assert a.moved == b.moved == set()
    assert a.order == b.order == 1


def test_features():

    sequence = [1, 2, 3, 0, 6, 5, 4]
    p = Perm(sequence)
    assert p.sequence() == sequence
    assert p.mapping == {0: 1, 1: 2, 2: 3, 3: 0, 4: 6, 6: 4}
    assert p.moved == {0, 1, 2, 3, 4, 6}
    assert p.cycles == [[0, 1, 2, 3], [4, 6]]
    assert p.order == 4
    assert p.inverse == Perm([3, 0, 1, 2, 6, 5, 4])

    sequence = [3, 2, 1, 0]
    p = Perm(sequence)
    assert p.sequence() == sequence
    assert p.mapping == {0: 3, 1: 2, 2: 1, 3: 0}
    assert p.moved == {0, 1, 2, 3}
    assert p.cycles == [[0, 3], [1, 2]]
    assert p.order == 2
    assert p.inverse == p

    cycles = [[0, 5, 4], [1, 7, 2, 8], [3, 6]]
    p = Perm(cycles)
    assert p.cycles == cycles
    assert p.sequence() == [5, 7, 8, 6, 0, 4, 3, 2, 1]
    assert p.mapping == {0: 5, 5: 4, 4: 0, 1: 7, 7: 2, 2: 8, 8: 1, 3: 6, 6: 3}
    assert p.moved == {0, 1, 2, 3, 4, 5, 6, 7, 8}
    assert p.order == 12
    assert p.inverse == Perm([4, 8, 7, 6, 5, 0, 3, 1, 2])


def test_slice():

    seq = [4, 3, 2, 1, 0]
    p = Perm(seq)
    assert p[:] == p[::] == p[:5] == p[0:5] == p[0:5:1] == seq


def test_concat():

    a_sequence = [1, 0, 2, 4, 3, 5, 7, 6, 8, 10, 9, 11, 13, 12, 14]
    b_sequence = [0, 1, 4, 3, 2, 5, 6, 9, 8, 7, 10, 11, 14, 13, 12]

    a = Perm(a_sequence)
    b = Perm(b_sequence)

    ab = a * b
    ba = b * a

    ab_sequence = [1, 0, 3, 4, 2, 5, 7, 10, 8, 6, 9, 11, 14, 12, 13]
    ba_sequence = [1, 0, 4, 2, 3, 5, 9, 6, 8, 10, 7, 11, 13, 14, 12]

    ab_cycles = [[0, 1], [2, 3, 4], [6, 7, 10, 9], [12, 14, 13]]
    ba_cycles = [[0, 1], [2, 4, 3], [6, 9, 10, 7], [12, 13, 14]]

    assert a.length == 14
    assert b.length == ab.length == ba.length == 15

    assert a.sequence(15) == a_sequence
    assert b.sequence() == b.sequence(15) == b_sequence

    assert ab.sequence(20) == ab_sequence + [15, 16, 17, 18, 19]
    assert ab.sequence() == ab_sequence
    assert ba.sequence() == ba_sequence

    assert ab.cycles == ab_cycles
    assert ba.cycles == ba_cycles

    assert ab.inverse == ba
    assert ba.inverse == ab

    abbrev(LengthTooSmallError, [
        lambda: ab.sequence(14)
    ])
