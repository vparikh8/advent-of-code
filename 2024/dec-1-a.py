if __name__ == "__main__":
    list1 = []
    list2 = []

    with open("input.txt") as fin:
        data = fin.read().split('\n')
    
    ans = 0

    for line in data:
        parts = line.split()
        list1.append(int(parts[0]))
        list2.append(int(parts[1]))

    for i in range(len(list1)):
        a = min(list1)
        list1.remove(min(list1))
        b = min(list2)
        list2.remove(min(list2))
        diff = abs(a-b)
        ans += diff

    print(ans)