def play(nums, n_turns):
	last_seen = [0] * n_turns
	prev = nums[-1]

	for turn, n in enumerate(nums[:-1], 1):
		last_seen[n] = turn

	for prev_turn in range(len(nums), n_turns):
		cur = prev_turn - last_seen[prev]
		if cur == prev_turn:
			cur = 0

		last_seen[prev] = prev_turn
		prev = cur

	return cur


with open("input.txt", "r") as fin:
	nums = tuple(map(int, fin.read().split(',')))

ans = play(nums, 2020)
print('Part 1:', ans)

ans = play(nums, 30000000)
print('Part 2:', ans)