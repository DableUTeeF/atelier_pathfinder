import json
import igraph as ig
from matplotlib import pyplot as plt
import numpy as np
import itertools


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
        path, all_paths = self.get_path(predecessors, start_vertex_data, end_vertex_data)
        return distances, distances[end_vertex], path, all_paths

    def get_path(self, predecessors, start_vertex, end_vertex):
        path = []
        current = self.vertex_data.index(end_vertex)
        while current is not None:
            path.insert(0, self.vertex_data[current])
            current = predecessors[current]
            if current == self.vertex_data.index(start_vertex):
                path.insert(0, start_vertex)
                break
        return '->'.join(path), path


def get_all_distances(src1, src2, src3, all_path_distances):
    all_distances1, distance1, path1, all_paths1 = g.dijkstra(src1, dst)
    for i, item in enumerate(all_paths1[1:-1]):
        all_distances2, distance2, path2, all_paths2 = g.dijkstra(src2, item)
        if src3 is None:
            all_path_distances[f'{path1}\n{path2}'] = distance1 + distance2
        else:
            all_distances3, distance3, path3, all_paths3 = g.dijkstra(src3, item)
            all_path_distances[f'{path1}\n{path2}\n{path3}'] = distance1 + distance2 + distance3
    all_distances2, distance2, path2, all_paths2 = g.dijkstra(src2, dst)
    all_distances3, distance3, path3, all_paths3 = g.dijkstra(src3, dst)
    all_path_distances[f'{path1}\n{path2}'] = distance1 + distance2 + distance3
    return all_path_distances


if __name__ == '__main__':
    data = json.load(open('jsons/ryza.json'))

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

    g = Graph(len(names))
    for i, name in enumerate(names):
        g.add_vertex_data(i, name)

    for edge in edges:
        g.add_edge(edge[0], edge[1])

    dst = 'Brave Emblem'
    srcs = ['Clean Water', 'Fertile Soil', 'Mushroom Powder']

    all_path_distances = {}

    for src1 in srcs:
        for src2 in srcs:
            for src3 in srcs:
                if src1 != src2 and src2 != src3 and src1 != src3:
                    all_path_distances = get_all_distances(src1, src2, src3, all_path_distances)
    for k, v in all_path_distances.items():
        print(k)
        print(v)
        print()


