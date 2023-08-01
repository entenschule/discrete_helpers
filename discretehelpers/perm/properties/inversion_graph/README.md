# inversion graph

This is usually called [permutation graph](https://en.wikipedia.org/wiki/Permutation_graph).

The vertices are the elements of the permutation,
and the edges are the elements of the [inversion set](../inversion_set).

While the inversion set is just a list of pairs,
this property shows the connected components of the graph.


```python
from discretehelpers.perm import Perm


p = Perm([3, 0, 2, 1, 6, 4, 7, 5])

assert p.inversion_set == [
    (0, 1), (0, 2), (0, 3), (2, 3), 
    (4, 5), (4, 7), (6, 7)
]

assert p.inversion_graph == {
    (0, 1, 2, 3): [(0, 1), (0, 2), (0, 3), (2, 3)], 
    (4, 5, 6, 7): [(4, 5), (4, 7), (7, 6)]
}
```
