# apply permutation on vector

See [this test](../../test/02_concat/b_wiki_examples) for examples.

```python
from perm import Perm


perm = Perm([2, 0, 1])
assert perm.apply_on_vector(['0', '1', '2']) == ['1', '2', '0']
```
