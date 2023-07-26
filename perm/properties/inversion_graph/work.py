import networkx as nx


def work(self):

    graph = nx.Graph()

    for pair in self.inversion_set:
        graph.add_edge(*pair)

    result = dict()

    for set_of_component_vertices in nx.connected_components(graph):
        component_graph = graph.subgraph(set_of_component_vertices)
        component_edges = sorted(component_graph.edges)
        component_vertices = tuple(sorted(set_of_component_vertices))
        result[component_vertices] = component_edges

    return result
