with open("input.txt", "r") as fin:
	numbers = tuple(map(int, fin.readlines()))

compls  = set()
for x in numbers:
	y = 2020 - x

	if x in compls:
		ans = x * y
		break

	compls.add(y)

print('Part 1:', ans)

for i, x in enumerate(numbers):
	compls = set()
	yz = 2020 - x

	for y in numbers[i + 1:]:
		z = yz - y

		if y in compls:
			ans = x * y * z
			break

		compls.add(z)

print('Part 2:', ans)