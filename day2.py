from itertools import combinations

with open('input.txt') as f:
    rows = [tuple(map(int, l.split())) for l in f]

checksum = sum(max(row) - min(row) for row in rows)

evenly_divisible_sum = sum(b//a if not b%a else 0 for row in rows for a, b in combinations(sorted(row), 2))

print(f'Part 1: {checksum}, Part 2: {evenly_divisible_sum}')