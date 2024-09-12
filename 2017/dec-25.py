import numpy as np


state = 'A'
steps = 12683008
tape = np.zeros(2*steps)
cursor = steps
for k in range(steps):
    val = tape[cursor]
    if state == 'A':
        if val == 0:
            tape[cursor] = 1
            cursor += 1
            state = 'B'
        elif val == 1:
            tape[cursor] = 0
            cursor -= 1
            state = 'B'
    elif state == 'B':
        if val == 0:
            tape[cursor] = 1
            cursor -= 1
            state = 'C'
        elif val == 1:
            tape[cursor] = 0
            cursor += 1
            state = 'E'
    elif state == 'C':
        if val == 0:
            tape[cursor] = 1
            cursor += 1
            state = 'E'
        elif val == 1:
            tape[cursor] = 0
            cursor -= 1
            state = 'D'
    elif state == 'D':
        if val == 0:
            tape[cursor] = 1
            cursor -= 1
            state = 'A'
        elif val == 1:
            tape[cursor] = 1
            cursor -= 1
            state = 'A'
    elif state == 'E':
        if val == 0:
            tape[cursor] = 0
            cursor += 1
            state = 'A'
        elif val == 1:
            tape[cursor] = 0
            cursor += 1
            state = 'F'
    elif state == 'F':
        if val == 0:
            tape[cursor] = 1
            cursor += 1
            state = 'E'
        elif val == 1:
            tape[cursor] = 1
            cursor += 1
            state = 'A'
print(np.sum(tape))