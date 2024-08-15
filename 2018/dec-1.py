with open("input.txt", "r") as fin:
	deltas = list(map(int, fin.readlines()))

done = False
freq = 0
seen = set()
seen.add(0)

for d in deltas:
	freq += d

	if not done and freq in seen:
		done = True

	seen.add(freq)

print('Part 1:', freq)

while not done:
	for d in deltas:
		freq += d

		if freq in seen:
			done = True
			break

		seen.add(freq)

print('Part 2:', freq)