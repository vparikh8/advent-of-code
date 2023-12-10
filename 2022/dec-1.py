

if __name__ == "__main__":
	with open("input-dec-1.txt", "r") as f:
		lines = f.readlines()

		current_max = 0
		temp = 0
		count = 0
		for line in lines:
			if line.strip():
				temp += int(line)
			else:
				if temp > current_max and temp < 71481:
					current_max = temp
					count += 1
				temp = 0

	print(current_max, count)
