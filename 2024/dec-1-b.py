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
        a = list1[i]
        b = list2.count(a)
        prod = a * b
        ans += prod

    print(ans)