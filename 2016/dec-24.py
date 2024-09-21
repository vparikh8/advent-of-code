from itertools import permutations
import networkx as nx
import numpy as np


with open('input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

G = nx.Graph()
interest = {}
for y, l in enumerate(lines):
    for x, s in enumerate(l):
        if s == '.' or s.isdigit():
            G.add_node((x, y))
            if s.isdigit():
                interest[int(s)] = (x, y)
            if y > 0 and (x, y - 1) in G:
                G.add_edge((x, y), (x, y - 1))
            if x > 0 and (x - 1, y) in G:
                G.add_edge((x, y), (x - 1, y))

# Pre-compute the shortest paths between all pairs of numbered locations.
lengths = np.empty((len(interest), len(interest)))
for i, node in interest.items():
    for j, node in interest.items():
        lengths[i, j] = len(nx.shortest_path(G, interest[i], interest[j])) - 1

# Part one
shortest = float('inf')
for p in permutations(range(1, len(interest))):
    length = lengths[0, p[0]]
    for i in range(len(p) - 1):
        length += lengths[p[i], p[i + 1]]
    shortest = min(shortest, length)
print(shortest)

# Part two
shortest = float('inf')
for p in permutations(range(1, len(interest))):
    length = lengths[0, p[0]]
    for i in range(len(p) - 1):
        length += lengths[p[i], p[i + 1]]
    length += lengths[p[-1], 0]
    shortest = min(shortest, length)
print(shortest)