def fuel2(nums, x):
    tot = 0
    for n in nums:
        delta = abs(n - x)
        tot += (delta * (delta + 1)) // 2
    return tot


with open("input.txt", mode="rt") as fin:
    nums = list(map(int, fin.readline().split(',')))

nums.sort()

median = nums[len(nums) // 2]
fuel   = sum(abs(x - median) for x in nums)

print('Part 1:', fuel)

mean = sum(nums) // len(nums)
fuel = min(fuel2(nums, mean), fuel2(nums, mean + 1))

print('Part 2:', fuel)