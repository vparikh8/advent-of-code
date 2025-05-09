import re


if __name__ == "__main__":
    with open("input.txt") as fin:
        data = fin.read().split('\n')
    
    ans = 0
    enabled = True
    pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
    instructions = re.findall(pattern, "".join(data))

    for inst in instructions:
        match inst[0]:
            case "do()":
                enabled = True
            case "don't()":
                enabled = False
            case _ if enabled:
                ans += int(inst[1]) * int(inst[2])

    print(ans)