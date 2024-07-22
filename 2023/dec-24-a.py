
from itertools import combinations


def read_data(filename):
    with open(filename, mode='r') as file:
        return [[tuple(map(int, (values.split(',')))) for values in line.split('@')] for line in file]


def check_if_hailstones_would_collide(hailstones, xy_min, xy_max):
    hailstone_pairs = combinations(hailstones, 2)
    collision_counter = 0

    for hailstone_pair in hailstone_pairs:
        ((px_a, py_a, _), (vx_a, vy_a, _)), ((px_b, py_b, _), (vx_b, vy_b, _)) = hailstone_pair

        m_a = vy_a / vx_a  # m is slope
        m_b = vy_b / vx_b

        if m_a == m_b:  # parallel lines
            continue

        b_a = py_a - m_a * px_a  # b is intercept, y = mx + b -> b = y - mx
        b_b = py_b - m_b * px_b

        x = (b_b - b_a) / (m_a - m_b)
        y = m_a * x + b_a

        t_a = (x - px_a) / vx_a
        t_b = (x - px_b) / vx_b

        if t_a < 0 or t_b < 0:  # collision would occur in the past if t < 0
            continue

        if xy_min <= y <= xy_max and xy_min <= x <= xy_max:
            collision_counter += 1

    return collision_counter


if __name__ == '__main__':
    hailstones_data = read_data('input.txt')
    result = check_if_hailstones_would_collide(hailstones_data, 200000000000000, 400000000000000)
    print(result)