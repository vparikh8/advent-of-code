if __name__ == "__main__":
	with open("input.txt", "r") as f:
		lines = f.readlines()

	horizontal = 0
	depth = 0
	aim = 0

	for line in lines:
		parts = line.split(" ")
		if parts[0] == "forward":
			horizontal += int(parts[1])
			depth += (int(parts[1]) * aim)
		elif parts[0] == "down":
			aim += int(parts[1])
		else:
			aim -= int(parts[1])

	print("Part 1:", horizontal * depth)
	print("Part 2:", horizontal * depth)
