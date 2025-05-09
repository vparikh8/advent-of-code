def find_diagonals(grid):
    rows, cols = len(grid), len(grid[0])

    # from top-left to bottom-right
    main_diagonals = {}

    # from top-right to bottom-left
    anti_diagonals = {}

    for r in range(rows):
        for c in range(cols):
            key_main = r - c
            if key_main not in main_diagonals:
                main_diagonals[key_main] = []
            main_diagonals[key_main].append(grid[r][c])

            key_anti = r + c
            if key_anti not in anti_diagonals:
                anti_diagonals[key_anti] = []
            anti_diagonals[key_anti].append(grid[r][c])

    return main_diagonals, anti_diagonals


if __name__ == "__main__":
    with open("input.txt") as fin:
        data = fin.read().split('\n')
    
    lines = data[:]
    lines.extend(["".join([row[i] for row in data]) for i in range(len(data[0]))])

    main_diagonals, anti_diagonals = find_diagonals(data)
    lines.extend(["".join(i) for i in main_diagonals.values()])
    lines.extend(["".join(i) for i in anti_diagonals.values()])

    print(sum(line.count("XMAS") + line.count("SAMX") for line in lines))