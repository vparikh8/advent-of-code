import re


def ways(t, d):
    count = 0
    for i in range(t):
        # Hold down for i seconds
        if (t - i) * i > d:
            count += 1

    return count


if __name__ == "__main__":
    with open("input.txt") as fin:
        lines = fin.read().strip().split("\n")

    t = int("".join(lines[0].split()[1:]))
    d = int("".join(lines[1].split()[1:]))

    print(ways(t, d))