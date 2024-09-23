with open('input.txt', 'r') as f:
    data = f.read()

result = 0
position = 1
for d in data:
    if d == '(':
        result += 1
    elif d == ')':
        result -= 1
    if result == -1:
        break
    position += 1

print("Part 1: ", result)
print("Part 2: ", position)