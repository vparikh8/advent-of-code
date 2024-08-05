from itertools import product


table  = str.maketrans('BFRL', '1010')
with open("input.txt", "r") as fin:
	seats  = fin.read().translate(table).splitlines()
	ids    = tuple(map(lambda s: int(s, 2), seats))
	max_id = max(ids)

print('Part 1:', max_id)

min_id   = min(ids)
expected = max_id * (max_id + 1) // 2 - min_id * (min_id - 1) // 2
my_id    = expected - sum(ids)

print('Part 2:', my_id)