with open('input.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]

x = y = z = result = ribbons = 0
for box in data:
    sides = box.split('x')
    sides = [int(x) for x in sides]
    x = sides[0] * sides[1]
    y = sides[0] * sides[2]
    z = sides[1] * sides[2]
    result += ((2*x) + (2*y) + (2*z) + min(x,y,z))
    print(sorted(sides))
    ribbons += (sorted(sides)[0] + sorted(sides)[0] + sorted(sides)[1] + sorted(sides)[1]) + (sides[0] * sides[1] * sides[2])

print("Part 1:", result)
print("Part 2:", ribbons)