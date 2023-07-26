# `Perm` (permutation)


```python
from perm import Perm


cycles = [[0, 3, 2, 1], [4, 6]]
sequence = [3, 0, 1, 2, 6, 5, 4]

p = Perm(cycles)
ps = Perm(sequence)
assert p == ps
assert p.length == 7
assert p.cycles == cycles
assert p.sequence() == p.sequence(7) == sequence
assert p.sequence(10) == sequence + [7, 8, 9]

assert p.moved == {0, 1, 2, 3, 4, 6}
assert p.mapping == {0: 3, 3: 2, 2: 1, 1: 0, 4: 6, 6: 4}

assert p.order == 4
assert p**2 == Perm([[0, 2], [1, 3]])
assert p**3 == Perm([[0, 1, 2, 3], [4, 6]])
assert p**4 == Perm()

assert p.inverse == p**-1 == p**3
```

Composition is from the left, i.e. `a * b` means `a` after `b`.<br>
The method `apply_on_vector` can be used to permute any list.<br>
See examples in the [tests](test), especially [here](test/02_concat/b_wiki_examples).
