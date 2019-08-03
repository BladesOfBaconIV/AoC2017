# https://www.redblobgames.com/grids/hexagons/ for explanation of positioning in hex grid

with open('input.txt') as f:
    steps = f.readline().split(',')

x = y = z = 0
delta_x_y_zs = {
    's': (0, -1, +1),
    'se': (+1, -1, 0),
    'sw': (-1, 0, +1),
    'n': (0, +1, -1),
    'ne': (+1, 0, -1),
    'nw': (-1, +1, 0),
}

dists = []
for s in steps:
    dx, dy, dz = delta_x_y_zs[s]
    x, y, z = x + dx, y + dy, z + dz
    dists.append((abs(x) + abs(y) + abs(z))//2)

print(f'Part 1: {dists[-1]}, Part 2: {max(dists)}')