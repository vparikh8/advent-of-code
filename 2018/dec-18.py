from collections import Counter


with open("input.txt", "r") as f:
    lines = [x.strip() for x in f.readlines()]

def update(d):
    new_d = {}
    for (x, y), t in d.items():
        adjacent = [d[(x + dx, y + dy)] for dx in (-1, 0, 1) for dy in (-1, 0, 1)
                    if (dx != 0 or dy != 0) and (x + dx, y + dy) in d]
        counter = Counter(adjacent)
        if t == '.':
            new_d[(x, y)] = '|' if counter['|'] >= 3 else '.'
        elif t == '|':
            new_d[(x, y)] = '#' if counter['#'] >= 3 else '|'
        elif t == '#':
            new_d[(x, y)] = '#' if counter['#'] >= 1 and counter['|'] >= 1 else '.'
    return new_d

initial_d = {(x, y): t for y, line in enumerate(lines) for x, t in enumerate(line)}

# Part one
d = dict(initial_d)
for _ in range(10):
    d = update(d)

c = Counter(d.values())
print(c['|'] * c['#'])

# Part two
d = dict(initial_d)
for i in range(1000):
    d = update(d)

c = Counter(d.values())
print(c['|'] * c['#'])