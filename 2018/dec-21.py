halters = []
e = 0
seen_d = set()
while True:
    d = e | 65536
    if d in seen_d:
        break
    seen_d.add(d)
    e = 13159625
    while True:
        c = d & 255
        e = c + e
        e &= 16777215
        e *= 65899
        e &= 16777215
        if 256 > d:
            halters.append(e)
            break
        else:
            d //= 256

# Part one
print(halters[0])

# Part two
print(halters[-1])