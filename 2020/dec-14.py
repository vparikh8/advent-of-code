import re
from itertools import product


def all_addrs(addr, mask):
	args = []

	for addr_bit, mask_bit in zip(addr, mask):
		if mask_bit == '0':
			args.append(addr_bit)
		elif mask_bit == '1':
			args.append('1')
		else:
			args.append('01')

	for a in product(*args):
		yield int(''.join(a), 2)


with open("input.txt", "r") as fin:
	lines = fin.readlines()

rexp  = re.compile(r'mem\[(\d+)\] = (\d+)')
table = str.maketrans('1X', '01')
mem1  = {}
mem2  = {}

for line in lines:
	if line.startswith('mask'):
		mask       = line[7:].rstrip()
		mask_clear = int(mask.translate(table), 2)
		mask_set   = int(mask.replace('X', '0'), 2)
	else:
		addr, value = map(int, rexp.findall(line)[0])
		mem1[addr]  = (value & mask_clear) | mask_set

		addr = '{:036b}'.format(addr)
		for a in all_addrs(addr, mask):
			mem2[a] = value

total1 = sum(mem1.values())
total2 = sum(mem2.values())

print('Part 1:', total1)
print('Part 2:', total2)