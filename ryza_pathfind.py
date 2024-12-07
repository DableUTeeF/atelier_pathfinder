import json
import igraph as ig
from matplotlib import pyplot as plt

palette = [[0, 192, 64], [0, 192, 64], [0, 64, 96], [128, 192, 192],
           [0, 64, 64], [0, 192, 224], [0, 192, 192], [128, 192, 64],
           [0, 192, 96], [128, 192, 64], [128, 32, 192], [0, 0, 224],
           [0, 0, 64], [0, 160, 192], [128, 0, 96], [128, 0, 192],
           [0, 32, 192], [128, 128, 224], [0, 0, 192], [128, 160, 192],
           [128, 128, 0], [128, 0, 32], [128, 32, 0], [128, 0, 128],
           [64, 128, 32], [0, 160, 0], [0, 0, 0], [192, 128, 160],
           [0, 32, 0], [0, 128, 128], [64, 128, 160], [128, 160, 0],
           [0, 128, 0], [192, 128, 32], [128, 96, 128], [0, 0, 128],
           [64, 0, 32], [0, 224, 128], [128, 0, 0], [192, 0, 160],
           [0, 96, 128], [128, 128, 128], [64, 0, 160], [128, 224, 128],
           [128, 128, 64], [192, 0, 32], [128, 96, 0], [128, 0, 192],
           [0, 128, 32], [64, 224, 0], [0, 0, 64], [128, 128, 160],
           [64, 96, 0], [0, 128, 192], [0, 128, 160], [192, 224, 0],
           [0, 128, 64], [128, 128, 32], [192, 32, 128], [0, 64, 192],
           [0, 0, 32], [64, 160, 128], [128, 64, 64], [128, 0, 160],
           [64, 32, 128], [128, 192, 192], [0, 0, 160], [192, 160, 128],
           [128, 192, 0], [128, 0, 96], [192, 32, 0], [128, 64, 128],
           [64, 128, 96], [64, 160, 0], [0, 64, 0], [192, 128, 224],
           [64, 32, 0], [0, 192, 128], [64, 128, 224], [192, 160, 0],
           [0, 192, 0], [192, 128, 96], [192, 96, 128], [0, 64, 128],
           [64, 0, 96], [64, 224, 128], [128, 64, 0], [192, 0, 224],
           [64, 96, 128], [128, 192, 128], [64, 0, 224], [192, 224, 128],
           [128, 192, 64], [192, 0, 96], [192, 96, 0], [128, 64, 192],
           [0, 128, 96], [0, 224, 0], [64, 64, 64], [128, 128, 224],
           [0, 96, 0], [64, 192, 192], [0, 128, 224], [128, 224, 0],
           [64, 192, 64], [128, 128, 96], [128, 32, 128], [64, 0, 192],
           [0, 64, 96], [0, 160, 128], [192, 0, 64], [128, 64, 224],
           [0, 32, 128], [192, 128, 192], [0, 64, 224], [128, 160, 128],
           [192, 128, 0], [128, 64, 32], [128, 32, 64], [192, 0, 128],
           [64, 192, 32], [0, 160, 64], [64, 0, 0], [192, 192, 160],
           [0, 32, 64], [64, 128, 128], [64, 192, 160], [128, 160, 64],
           [64, 128, 0], [192, 192, 32], [128, 96, 192], [64, 0, 128],
           [64, 64, 32], [0, 224, 192], [192, 0, 0], [192, 64, 160],
           [0, 96, 192], [192, 128, 128], [64, 64, 160], [128, 224, 192],
           [192, 128, 64], [192, 64, 32], [128, 96, 64], [192, 0, 192],
           [0, 192, 32], [64, 224, 64], [64, 0, 64], [128, 192, 160],
           [64, 96, 64], [64, 128, 192], [0, 192, 160], [192, 224, 64],
           [64, 128, 64], [128, 192, 32], [192, 32, 192], [64, 64, 192],
           [0, 64, 32], [64, 160, 192], [192, 64, 64], [128, 64, 160],
           [64, 32, 192], [192, 192, 192], [0, 64, 160], [192, 160, 192],
           [192, 192, 0], [128, 64, 96], [192, 32, 64], [192, 64, 128],
           [64, 192, 96], [64, 160, 64], [64, 64, 0]]


class Graph:
    """
    From https://www.w3schools.com/dsa/dsa_algo_graphs_dijkstra.php
    """
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def dijkstra(self, start_vertex_data, end_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        end_vertex = self.vertex_data.index(end_vertex_data)
        distances = [float('inf')] * self.size
        predecessors = [None] * self.size
        distances[start_vertex] = 0
        visited = [False] * self.size

        for _ in range(self.size):
            min_distance = float('inf')
            u = None
            for i in range(self.size):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i

            if u is None or u == end_vertex:
                break

            visited[u] = True

            for v in range(self.size):
                if self.adj_matrix[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.adj_matrix[u][v]
                    if alt < distances[v]:
                        distances[v] = alt
                        predecessors[v] = u

        return distances[end_vertex], self.get_path(predecessors, start_vertex_data, end_vertex_data)

    def get_path(self, predecessors, start_vertex, end_vertex):
        path = []
        current = self.vertex_data.index(end_vertex)
        while current is not None:
            path.insert(0, self.vertex_data[current])
            current = predecessors[current]
            if current == self.vertex_data.index(start_vertex):
                path.insert(0, start_vertex)
                break
        return '->'.join(path)


def plot_ig():
    g = ig.Graph(
        len(data),
        edges,
        directed=True
    )

    fig, ax = plt.subplots()
    ig.plot(
        g,
        target=ax,
        vertex_size=30,
        vertex_label=names,
        vertex_color=colors,
    )
    plt.show()


if __name__ == '__main__':
    data = json.load(open('jsons/ryza.json'))
    src1 = 'Uni'
    dst = 'Prosthetic Arm'

    source = data[src1]
    destination = data[dst]

    categories = {}
    item2idx = {}
    for name, item in data.items():
        item2idx[name] = len(item2idx)
        for cat in item['categories']:
            if cat.startswith('('):
                if cat not in categories:
                    categories[cat] = {'items': [], 'color': [c / 255 for c in palette[len(categories)]]}
                categories[cat]['items'].append(name)

    edges = []
    colors = []
    names = []
    for name, item in data.items():
        names.append(name)
        colors.append(categories[item['categories'][0]]['color'])
        if 'ingredients' in item:
            for ing in item['ingredients']:
                if ing.startswith('('):
                    for cat in categories[ing]['items']:
                        edges.append((item2idx[cat], item2idx[name]))
                else:
                    edges.append((item2idx[ing], item2idx[name]))

    # plot_ig()

    g = Graph(len(names))
    for i, name in enumerate(names):
        g.add_vertex_data(i, name)

    for edge in edges:
        g.add_edge(edge[0], edge[1])

    distance, path = g.dijkstra('Clean Water', 'Bomb')
    print(f"Path: {path}, Distance: {distance}")
