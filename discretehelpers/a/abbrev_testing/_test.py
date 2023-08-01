from discretehelpers.a import abbrev_testing


class NoArgError(ValueError):
    """You need to provide an argument."""


class NotFiveError(ValueError):
    """The argument must be 5."""


# example class
class Hand:
    def __init__(self, give_me_five=None):
        if give_me_five is None:
            raise NoArgError
        if give_me_five != 5:
            raise NotFiveError
        self.twice_five = 2 * give_me_five


def test_raise():
    abbrev_testing(NoArgError, [
        lambda: Hand()
    ])

    abbrev_testing(NotFiveError, [
        lambda: Hand(0),
        lambda: Hand(6),
        lambda: Hand(''),
        lambda: Hand('5')
    ])


def test_values():
    assert Hand(5).twice_five == 10
