
from collections import defaultdict
from math import prod
from copy import deepcopy
import random


def read_data(filename):
    with open(filename, mode='r') as file:
        graph = defaultdict(list)
        for line in file:
            source, *destinations = line.replace(':', '').split()
            graph[source] += destinations
            for destination in destinations:
                graph[destination].append(source)
    return graph


def karger_algorithm(graph):
    vertices_count = {key: 1 for key in graph.keys()}

    while len(graph) > 2:
        u = random.choice(list(graph.keys()))
        v = random.choice(graph[u])

        graph[u] += graph[v]

        # update all occurrences of v to u in the graph
        for neighbor in graph[v]:
            graph[neighbor].remove(v)
            graph[neighbor].append(u)

        # remove self-loops
        graph[u] = [vertex for vertex in graph[u] if vertex != u]

        del graph[v]

        vertices_count[u] += vertices_count[v]
        del vertices_count[v]

    return len(graph[list(graph.keys())[0]]), prod(vertices_count.values())


if __name__ == '__main__':
    graph_data = read_data('input.txt')
    # graph_data = read_data('../test_input/25.txt')  # 54

    min_cut = 0
    result = None

    while min_cut != 3:
        graph_copy = deepcopy(graph_data)
        min_cut, result = karger_algorithm(graph_copy)

    print(result)