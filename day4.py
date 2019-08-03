with open('input.txt') as f:
    phrases = [l.strip().split() for l in f]

no_dups = lambda x: len(x) == len(set(x))
no_acrs = lambda x: len(x) == len(set(''.join(sorted(y)) for y in x))
both = lambda x: no_dups(x) and no_acrs(x)

print(f'Part 1: {sum(no_dups(p) for p in phrases)}, Part 2: {sum(both(p) for p in phrases)}')