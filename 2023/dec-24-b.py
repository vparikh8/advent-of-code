import pathlib


def reader():
  f = open("input.txt", 'r').read()
  f = f.split('\n')
  f = f[:-1]
  return f

def part2():
  f = [tuple(map(eval, s.split(' @ '))) for s in reader()]

  def add(l1, l2):
    return [l1[i] + l2[i] for i in range(len(l1))]

  def mul(l1, s):
    return [s * l1[i] for i in range(len(l1))]

  def dot(l1, l2):
    return sum([l1[i] * l2[i] for i in range(len(l1))])

  def cross(l1, l2):
    return [l1[1] * l2[2] - l1[2] * l2[1], l1[2] *
            l2[0] - l1[0] * l2[2], l1[0] * l2[1] - l1[1] * l2[0]]

  p1, v1 = (add(f[0][0], mul(f[2][0], -1)), add(f[0][1], mul(f[2][1], -1)))
  p2, v2 = (add(f[1][0], mul(f[2][0], -1)), add(f[1][1], mul(f[2][1], -1)))

  t1 = -dot(cross(p1, p2), v2) // \
      dot(cross(v1, p2), v2)
  t2 = -dot(cross(p1, p2), v1) // \
      dot(cross(p1, v2), v1)
  c1 = add(f[0][0], mul(f[0][1], t1))
  c2 = add(f[1][0], mul(f[1][1], t2))
  p = add(c1, mul(mul(add(c2, mul(c1, -1)), 1 / (t2 - t1)), -t1))
  print(round(sum(p)))

part2()