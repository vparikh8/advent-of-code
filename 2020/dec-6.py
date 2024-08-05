with open("input.txt", "r") as fin:
	groups = fin.read().split('\n\n')
	groups = tuple(map(lambda g: tuple(map(set, g.splitlines())), groups))

n_any_yes = sum(len(set.union(*g)) for g in groups)
n_all_yes = sum(len(set.intersection(*g)) for g in groups)

print('Part 1:', n_any_yes)
print('Part 2:', n_all_yes)