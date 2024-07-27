with open("input.txt") as fin:
    lines = fin.read().strip().splitlines()

LONGEST = max([len(line) for line in lines])
MAP = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
MAP_REV = {v: k for k, v in MAP.items()}

# least significant figure first and 0 padded to max length
snafus = [
    [MAP[char] for char in line[::-1]] + [0] * (LONGEST - len(line))
    for line in lines
]
ts = [sum(vs) for vs in zip(*snafus)]  # total for each column ignoring any carry over

out = ""
carry_over = co = 0
for t in ts:
    nco, r = divmod(t + co, 5)
    if r > 2:
        r -= 5
        nco += 1
    co = nco
    out = MAP_REV[r] + out

print(out)