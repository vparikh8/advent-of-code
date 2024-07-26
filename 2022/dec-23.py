from collections import deque
from datetime import datetime

start_time = datetime.now()

with open("input.txt") as fin:
    lines = fin.read().strip().splitlines()

dirs = deque(
    [
        (-1j, (-1 - 1j, -1j, 1 - 1j)),
        (1j, (-1 + 1j, 1j, 1 + 1j)),
        (-1, (-1 - 1j, -1, -1 + 1j)),
        (1, (1 - 1j, 1, 1 + 1j)),
    ]
)

ALL_DIRS = []
for _, ds in dirs:
    ALL_DIRS.extend(list(ds))

elves = set()
for j, line in enumerate(lines):
    for i, char in enumerate(line):
        if char == "#":
            elves.add(complex(i, j))

for _ in range(10):
    once = set()
    twice = set()
    for elf in elves:
        if not any(elf + d in elves for d in ALL_DIRS):
            continue

        for d, view_dirs in dirs:
            if not any(elf + view_dir in elves for view_dir in view_dirs):
                nelf = elf + d
                if nelf in once:
                    twice.add(nelf)
                else:
                    once.add(nelf)
                break
    
    elves_copy = elves.copy()
    for elf in elves_copy:
        if not any(elf + d in elves_copy for d in ALL_DIRS):
            continue

        for d, view_dirs in dirs:
            if not any(elf + view_dir in elves_copy for view_dir in view_dirs):
                nelf = elf + d
                if nelf not in twice:
                    elves.remove(elf)
                    elves.add(nelf)
                break

    dirs.rotate(-1)

cs = max(elf.real for elf in elves) - min(elf.real for elf in elves) + 1
rs = max(elf.imag for elf in elves) - min(elf.imag for elf in elves) + 1
print(int((cs * rs) - len(elves)))

# # part b, same approach as part a, breaking now when no elves to move

dirs = deque(
    [
        (-1j, (-1 - 1j, -1j, 1 - 1j)),
        (1j, (-1 + 1j, 1j, 1 + 1j)),
        (-1, (-1 - 1j, -1, -1 + 1j)),
        (1, (1 - 1j, 1, 1 + 1j)),
    ]
)

ALL_DIRS = []
for _, ds in dirs:
    ALL_DIRS.extend(list(ds))

elves = set()
for j, line in enumerate(lines):
    for i, char in enumerate(line):
        if char == "#":
            elves.add(complex(i, j))

rnd = 0
while True:
    rnd += 1
    once = set()
    twice = set()
    for elf in elves:
        if not any(elf + d in elves for d in ALL_DIRS):
            continue

        for d, view_dirs in dirs:
            if not any(elf + view_dir in elves for view_dir in view_dirs):
                nelf = elf + d
                if nelf in once:
                    twice.add(nelf)
                else:
                    once.add(nelf)
                break

    if not once:
        break

    elves_copy = elves.copy()
    for elf in elves_copy:
        if not any(elf + d in elves_copy for d in ALL_DIRS):
            continue

        for d, view_dirs in dirs:
            if not any(elf + view_dir in elves_copy for view_dir in view_dirs):
                nelf = elf + d
                if nelf not in twice:
                    elves.remove(elf)
                    elves.add(nelf)
                break

    dirs.rotate(-1)

print(rnd)