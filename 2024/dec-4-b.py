if __name__ == "__main__":
    with open("input.txt") as fin:
        data = fin.read().split('\n')
    
    rows, cols = len(data), len(data[0])
    ans = 0

    _set = {"M", "S"}

    # find A as center of the cross, then check the diagonals
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if data[r][c] == "A":
                if {data[r - 1][c - 1], data[r + 1][c + 1]} == _set and {data[r - 1][c + 1], data[r + 1][c - 1]} == _set:
                    ans += 1

    print(ans)