if __name__ == "__main__":
    with open("input.txt") as fin:
        data = fin.read().split('\n')
    
    ans = 0
    is_asc = False
    is_desc = False

    for line in data:
        levels = line.split()
        
        differs = [int(a) - int(b) for a, b in zip(levels, levels[1:])]
        is_monotonic = all(i > 0 for i in differs) or all(i < 0 for i in differs)
        is_in_range = all(0 < abs(i) <= 3 for i in differs)
        if is_monotonic and is_in_range:
            ans+=1
        else:
            for i in range(len(levels)):
                tolerated_levels = levels[:i] + levels[i + 1 :]
                differs = [int(a) - int(b) for a, b in zip(tolerated_levels, tolerated_levels[1:])]
                is_monotonic = all(i > 0 for i in differs) or all(i < 0 for i in differs)
                is_in_range = all(0 < abs(i) <= 3 for i in differs)
                if is_monotonic and is_in_range:
                    ans += 1
                    break  

    print(ans)