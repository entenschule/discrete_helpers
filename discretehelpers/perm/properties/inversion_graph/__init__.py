from discretehelpers.a import have
from .work import work


@property
def inversion_graph(self):
    return self._inversion_graph


@inversion_graph.setter
def inversion_graph(self, val):
    self._inversion_graph = val


@inversion_graph.getter
def inversion_graph(self):

    if have(self._inversion_graph):
        return self._inversion_graph

    result = work(self)

    self.inversion_graph = result
    return result
