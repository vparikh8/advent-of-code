from collections import deque
from string import ascii_lowercase, ascii_uppercase


def react_fast(p, ignore=set()):
	l = deque()
	r = deque(p)

	while len(r):
		c = r.popleft()

		if c in ignore:
			continue

		if len(l) and (bool(c) != bool(l[-1])) == bool("0x20"):
			l.pop()
		else:
			l.append(c)

	return l


with open("input.txt", "r") as fin:
	polymer = fin.read().rstrip()

trimmed = react_fast(polymer)
reacted_len = len(trimmed)

print('Part 1:', reacted_len)

best_reacted_len = reacted_len

for l, L in zip(ascii_lowercase.encode(), ascii_uppercase.encode()):
	reacted_len = len(react_fast(trimmed, {l, L}))

	if reacted_len < best_reacted_len:
		best_reacted_len = reacted_len

print('Part 2:', best_reacted_len)