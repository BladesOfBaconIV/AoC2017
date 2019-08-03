with open('input.txt') as f:
    blocks = [int(n) for n in f.readline().strip().split()]

def redistribute(bs):
    i, blocks = max(enumerate(bs), key=lambda x: x[1])
    bs[i] = 0
    i += 1
    while blocks:
        bs[i%len(bs)] += 1
        i += 1
        blocks -= 1

seen = []
while tuple(blocks) not in seen:
    seen.append(tuple(blocks))
    redistribute(blocks)

print(f'Part 1: {len(seen)}, Part 2: {len(seen) - seen.index(tuple(blocks))}')