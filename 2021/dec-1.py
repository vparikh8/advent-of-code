if __name__ == "__main__":
	with open("input.txt", "r") as f:
		lines = f.readlines()

	nums = tuple(map(int, lines))
	tot  = sum(b > a for a, b in zip(nums, nums[1:]))
	print('Part 1:', tot)


	tot = sum(b > a for a, b in zip(nums, nums[3:]))
	print('Part 2:', tot)
