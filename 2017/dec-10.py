import numpy as np


# Part one
arr = np.arange(256)
arrlen = len(arr)
skip_size = 0
head = 0
lengths = [225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110]
for l in lengths:
    newarr = np.copy(arr)
    for i in range(l):
        newarr[(head + i) % arrlen] = arr[(head + l - i - 1) % arrlen]
    arr = newarr
    head += (l + skip_size) % arrlen
    skip_size += 1
print(arr[0]*arr[1])

# Part 2
s = ','.join(map(str, lengths))
lengths = [ord(x) for x in s] + [17, 31, 73, 47, 23]
arr = np.arange(256)
arrlen = len(arr)
skip_size = 0
head = 0
for _ in range(64):
    for l in lengths:
        newarr = np.copy(arr)
        for i in range(l):
            newarr[(head + i) % arrlen] = arr[(head + l - i - 1) % arrlen]
        arr = newarr
        head += l + skip_size
        skip_size += 1
print(''.join(hex(x)[2:].zfill(2) for x in np.bitwise_xor.reduce(arr.reshape(16, 16), axis=1)))