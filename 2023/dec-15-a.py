if __name__ == "__main__":
    with open("input.txt") as fin:
        lines = fin.read().strip().split(",")

    ans = 0
    total = 0
    for line in lines:
        for c in line:
            ans += ord(c)
            ans *= 17
            ans %= 256
        total += ans
        ans = 0

    print(total)