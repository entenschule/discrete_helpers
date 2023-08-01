from itertools import combinations


def work(self):

    result = []

    for a, b in combinations(range(self.length), 2):
        if self[a] > self[b]:
            result.append((a, b))

    return sorted(result)
