from collections import Counter
import re


MOVEMAP = {
	'e' : ( 1,  0),
	'w' : (-1,  0),
	'se': ( 1,  1),
	'sw': ( 0,  1),
	'ne': ( 0, -1),
	'nw': (-1, -1)
}

def walk(moves):
	x, y = 0, 0

	for move in moves:
		dx, dy = MOVEMAP[move]
		x += dx
		y += dy

	return x, y

def evolve(grid):
	deltas = ((1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1))
	near = Counter((x + dx, y + dy) for x, y in grid for dx, dy in deltas)
	return set(p for p, n in near.items() if n == 2 or n == 1 and p in grid)


grid = set()
rexp = re.compile(r'e|w|se|sw|ne|nw')
with open("input.txt", "r") as fin:
	for line in fin:
		moves = rexp.findall(line)
		p = walk(moves)

		if p in grid:
			grid.remove(p)
		else:
			grid.add(p)

n_black = len(grid)
print('Part 1:', n_black)

for _ in range(100):
	grid = evolve(grid)

n_black = len(grid)
print('Part 2:', n_black)