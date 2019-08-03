with open('input.txt') as f:
    jumps = [int(l.strip()) for l in f]

def calc_steps(jumps, inc_func=lambda x: x + 1):
    skip = i = steps = 0
    N = len(jumps)
    while i < N:
        next_jump = i + jumps[i]
        jumps[i] = inc_func(jumps[i])
        i, steps = next_jump, steps + 1
    return steps

print(f'Part 1: {calc_steps(jumps[:])}, Part 2: {calc_steps(jumps, lambda x: x + 1 if x < 3 else x - 1)}')
