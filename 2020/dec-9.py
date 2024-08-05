def two_sum(nums, target):
	compls = set()

	for x in nums:
		if x in compls:
			return True

		compls.add(target - x)

	return False


with open("input.txt", "r") as fin:
	nums = tuple(map(int, fin.readlines()))

for i, target in enumerate(nums[25:]):
	if not two_sum(nums[i:i + 25], target):
		break

print('Part 1:', target)

cusums = [0]
a, b = 0, 0

while 1:
	partsum = cusums[b] - cusums[a]

	if partsum < target:
		cusums.append(cusums[-1] + nums[b])
		b += 1
	elif partsum > target:
		a += 1
	else:
		break

subseq = nums[a:b + 1]
ans = min(subseq) + max(subseq)

print('Part 2:', ans)