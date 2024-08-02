from operator import itemgetter

def fold(sheet, axis, vertical=False):
    folded = set()

    for x, y in sheet:
        if vertical:
            if x > axis:
                x = axis - (x - axis)
        elif y > axis:
            y = axis - (y - axis)

        folded.add((x, y))

    return folded

def print_sheet(sheet):
    maxx = max(map(itemgetter(0), sheet))
    maxy = max(map(itemgetter(1), sheet))

    out = ''
    for y in range(maxy + 1):
        for x in range(maxx + 1):
            out += '#' if (x, y) in sheet else ' '
        out += '\n'

    print(out, end='')
    

sheet = set()

with open("input.txt", mode="rt") as fin:
    for line in fin:
        if line == '\n':
            break

        sheet.add(tuple(map(int, line.split(','))))

    line     = next(fin)
    axis     = int(line[line.index('=') + 1:])
    sheet    = fold(sheet, axis, 'x' in line)
    n_points = len(sheet)

    for line in fin:
        axis  = int(line[line.index('=') + 1:])
        sheet = fold(sheet, axis, 'x' in line)

print('Part 1:', n_points)
print('Part 2:')
print_sheet(sheet)