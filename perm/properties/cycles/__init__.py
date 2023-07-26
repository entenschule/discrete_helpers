from a import have


@property
def cycles(self):
    return self._cycles


@cycles.setter
def cycles(self, val):
    self._cycles = val


@cycles.getter
def cycles(self):

    if have(self._cycles):
        return self._cycles

    if self.neutral:
        self.cycles = []
        return []

    mapping = self.mapping.copy()
    result = []
    while len(mapping) > 0:
        cycle = []
        key = sorted(mapping.keys())[0]
        cycle.append(key)
        while True:
            old_key = key
            key = mapping[key]
            del mapping[old_key]
            if key not in cycle:
                cycle.append(key)
            else:
                result.append(cycle)
                break

    self.cycles = result
    return result
