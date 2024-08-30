import numpy as np


banks = np.array([4,10,4,1,8,4,9,14,5,1,14,15,0,15,3,5], dtype=np.int32)
seen_banks = []
num_banks = len(banks)
cycles = 0

while True:
    seen_banks.append(np.copy(banks))
    highest = np.argmax(banks)
    blocks = banks[highest]
    rounds = blocks // num_banks
    extra = blocks % num_banks
    indices = (highest + 1 + np.arange(extra)) % (num_banks)
    banks[highest] = 0
    banks[indices] += 1
    banks += np.repeat(rounds, num_banks)
    if any(np.all(old_banks == banks) for old_banks in seen_banks):
        break

# Part one
print(len(seen_banks))

# Part two
print(len(seen_banks) - np.argmax([np.all(old_banks == banks) for old_banks in seen_banks]))