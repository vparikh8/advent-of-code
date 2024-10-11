from itertools import combinations, count
import numpy as np


with open('input.txt', 'r') as f:
    lines = [int(l.strip()) for l in f.readlines()]


def solve(part_one):
    s = sum(lines)
    target = s // 3 if part_one else s // 4
    for i in count():
        c = combinations(lines, i)
        m = float('inf')
        for g1 in c:
            if sum(g1) != target:
                continue
            m = min(m, np.product(g1))
        if m < float('inf'):
            return m


print(solve(True))
print(solve(False))