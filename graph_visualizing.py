import igraph as ig
from matplotlib import pyplot as plt
import random


if __name__ == '__main__':
    random.seed(0)
    g = ig.Graph.Lattice([6, 6], circular=False)
    layout = g.layout("grid")
    permutation = list(range(g.vcount()))
    random.shuffle(permutation)
    g = g.permute_vertices(permutation)
    new_layout = g.layout("grid")
    for i in range(36):
        new_layout[permutation[i]] = layout[i]
    layout = new_layout
    spanning_tree = g.spanning_tree(weights=None, return_tree=False)
    g.es["color"] = "lightgray"
    g.es[spanning_tree]["color"] = "midnightblue"
    g.es["width"] = 0.5
    g.es[spanning_tree]["width"] = 3.0

    fig, ax = plt.subplots()
    ig.plot(
        g,
        target=ax,
        layout=layout,
        vertex_color="lightblue",
        edge_width=g.es["width"]
    )
    plt.show()
