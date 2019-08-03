from day10 import knot_hash

KEY = 'ffayrhll'

def hex_to_bin(hex):
    return ''.join(f'{int(c, 16):04b}' for c in hex)

rows = []
for i in range(128):
    rows.append(list(hex_to_bin(knot_hash(f'{KEY}-{i}'))))

# Based on https://leetcode.com/problems/number-of-islands/discuss/56349/7-lines-Python-~14-lines-Java
def num_groups(grid):
    def sink(i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
            grid[i][j] = '0'
            list(map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1)))
            return 1
        return 0
    return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))

print(f'Part 1: {sum(c=="1" for r in rows for c in r)}, Part 2: {num_groups(rows)}')