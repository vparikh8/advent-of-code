def cmp(a, b):
    match a, b:
        case int(), int():
            return (a > b) - (a < b)
        case int(), list():
            return cmp([a], b)
        case list(), int():
            return cmp(a, [b])
        case list(), list():
            return next(filter(bool, map(cmp, a, b)), cmp(len(a), len(b)))


def count_le(packet):
    return sum(cmp(packet, x) == 1 for pair in pairs for x in pair) + 1


if __name__ == '__main__':
    with open("input.txt") as file:
        lines = file.read().strip()

    pairs = [[*map(eval, pair.split())] for pair in lines.split("\n\n")]

    print("Part 1:", sum(i for i, pair in enumerate(pairs, 1) if cmp(*pair) == -1))
    print("Part 2:", count_le([[2]]) * (count_le([[6]]) + 1))