WIDTH, HEIGHT = 25, 6
SIZE = WIDTH * HEIGHT


with open("input.txt", "r") as fin:
	chars = fin.readline().strip()

layers = [chars[i:i + SIZE] for i in range(0, len(chars), SIZE)]
best = min(layers, key=lambda l: l.count('0'))
checksum = best.count('1') * best.count('2')
print('Part 1:', checksum)

image = ['2'] * SIZE

for i in range(SIZE):
	for l in layers:
		if l[i] != '2':
			image[i] = l[i]
			break

conv = {'0': ' ', '1': '#'}
decoded = ''

for i in range(0, SIZE, WIDTH):
	decoded += ''.join(map(conv.get, image[i:i + WIDTH])) + '\n'

print('Part 2:', '\n' + decoded)