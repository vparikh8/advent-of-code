def HASH(input, multiplier = 17, divider =256):
    val = 0
    for i in input:
        val += ord(i)
        val *= multiplier
        val %= divider
    return val


if __name__ == "__main__":
    with open("input.txt") as fin:
        lines = fin.read().split(",")

    boxdict = {i: {} for i in range(0,256)}
    for line in lines:
        if "=" in line:
            line = line.split("=")
            boxdict[HASH(line[0])][line[0]] = int(line[1])

        else:
            line = line.replace("-","")
            boxdict[HASH(line)].pop(line, None)

    focus_power = 0
    for box, items in enumerate(boxdict.values()):
        for i, value in enumerate(items.values()):
            focus_power += (box + 1) * (i + 1) * value
    print(focus_power)