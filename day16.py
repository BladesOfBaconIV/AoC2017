from collections import deque
from string import ascii_lowercase

with open('input.txt') as f:
    moves = f.readline().strip().split(',')

def dance(start):
    programs = deque(start)
    for move in moves:
        o, args = move[0], move[1:]
        if o == 's':
            programs.rotate(int(args))
        elif o == 'x':
            a, b = map(int, args.split('/'))
            programs[a], programs[b] = programs[b], programs[a]
        else:
            a, b = map(programs.index, args.split('/'))
            programs[a], programs[b] = programs[b], programs[a]
    return ''.join(programs)

programs = ascii_lowercase[:16]
seen = set()
for i in range(1000000000):
    programs = dance(programs)
    if programs in seen:
        break
    seen.add(programs)

for _ in range(1000000000%len(seen)-1):
    programs = dance(programs)

print(f'Part 1: {dance(ascii_lowercase[:16])}, Part 2: {programs}')
    
