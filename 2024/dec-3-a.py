import re


if __name__ == "__main__":
    with open("input.txt") as fin:
        data = fin.read().split('\n')
    
    ans = 0
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    for line in data:
        matches = re.findall(pattern, "".join(line))
        ans += sum(int(x) * int(y) for x, y in matches)

    print(ans)