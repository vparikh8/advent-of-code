import re


with open("input.txt", "r") as fin:
	data     = fin.read()

rexp     = re.compile(r'(\d+)-(\d+) (\w): (\w+)')
policies = rexp.findall(data)

valid1, valid2 = 0, 0

for mmin, mmax, letter, password in policies:
	mmin, mmax = int(mmin), int(mmax)

	if mmin <= password.count(letter) <= mmax:
		valid1 += 1

	if (password[mmin - 1] == letter) ^ (password[mmax - 1] == letter):
		valid2 += 1

print('Part 1:', valid1)
print('Part 2:', valid2)