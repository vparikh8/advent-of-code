from math import ceil, sqrt


def bsgs(base, n, p):
	m     = ceil(sqrt(p))
	table = {pow(base, i, p): i for i in range(m)}
	inv   = pow(base, (p - 2) * m, p)
	res   = None

	for i in range(m):
		y = (n * pow(inv, i, p)) % p
		if y in table:
			res = i * m + table[y]
			break

	return res


with open("input.txt", "r") as fin:
	A, B = map(int, fin)

a    = bsgs(7, A, 20201227)
key  = pow(B, a, 20201227)

print('Part 1:', key)