import re


with open('input.txt', 'r') as f:
    data = f.read().strip()

# Part one
def find_length(s):
    length = 0
    state = 0
    i = 0
    while i < len(s):
        l = s[i]
        if state == 0 and l == '(':
            state = 1
            chars = ''
        elif state == 1 and l != 'x':
            chars += l
        elif state == 1 and l == 'x':
            state = 2
            reps = ''
        elif state == 2 and l != ')':
            reps += l
        elif state == 2 and l == ')':
            i += int(chars)
            length += int(chars) * int(reps) - 3 - len(chars) - len(reps)
            state = 0
        length += 1
        i += 1
    return length

print(find_length(data))

# Part two
def find_length_2(s):
    state = 0
    i = 0
    inner_lengths = 0
    while i < len(s):
        l = s[i]
        if state == 0 and l == '(':
            state = 1
            chars = ''
        elif state == 1 and l != 'x':
            chars += l
        elif state == 1 and l == 'x':
            state = 2
            reps = ''
        elif state == 2 and l != ')':
            reps += l
        elif state == 2 and l == ')':
            new_i = i + 1
            before_paren = s[:i - (2 + len(chars) + len(reps))]
            inner_lengths += find_length_2(s[i + 1:i + 1 + int(chars)]) * int(reps)
            after_repeated = s[i + 1 + int(chars):]
            s = before_paren + after_repeated
            i = len(before_paren) - 1
            state = 0
        i += 1
    return len(s) + inner_lengths

print(find_length_2(data))