from discretehelpers.a import true_except, is_natural, have

from discretehelpers.perm.ex import ArgTypeError, SequenceError, CyclesError, DictError, OtherNotPermError, LengthTooSmallError


class Perm(object):

    def __init__(self, arg=None):

        if not have(arg) or arg == list():
            self.make_neutral()
            return

        true_except(type(arg) in [list, tuple, dict], ArgTypeError)

        mapping = dict()
        if arg and type(arg) in [list, tuple]:  # if non-empty list or tuple
            element_type = type(arg[0])
            if element_type == int:  # `arg` is sequence, i.e. lower line of two-line notation
                true_except(sorted(arg) == list(range(len(arg))), SequenceError)
                for key, val in enumerate(arg):
                    if key != val:
                        mapping[key] = val
            elif element_type == list:  # `arg` is list of cycles
                for cycle in arg:
                    true_except(type(cycle) == list and all(is_natural(e) for e in cycle), CyclesError)
                    length = len(cycle)
                    for key, val in enumerate(cycle):
                        map_from = val
                        map_to = cycle[(key + 1) % length]
                        if map_from != map_to:
                            mapping[map_from] = map_to
        elif type(arg) == dict:
            true_except(sorted(arg.keys()) == sorted(arg.values()), DictError)
            for key, val in arg.items():
                if key != val:
                    mapping[key] = val

        if not mapping:
            self.make_neutral()
            return

        self.neutral = False
        self.mapping = mapping
        self.moved = set(self.mapping.keys())
        self.length = max(self.moved) + 1 if not self.neutral else 0
        self.set_dummies()

    def make_neutral(self):
        self.neutral = True
        self.mapping = dict()
        self.moved = set()
        self.length = 0
        self.set_dummies()

    def set_dummies(self):
        property_names = ['cycles', 'inverse', 'inversion_graph', 'inversion_set', 'order', 'parity']
        for name in property_names:
            setattr(self, '_' + name, None)

    from discretehelpers.perm.properties import cycles, inverse, inversion_graph, inversion_set, order, parity

    from discretehelpers.perm.methods import __getitem__, __eq__, __str__, __repr__, __hash__, __mul__, __pow__, \
        apply_on_vector, sequence
