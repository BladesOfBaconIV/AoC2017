from collections import defaultdict

registers = defaultdict(int)
max_reg = 0

with open('input.txt') as f:
    for line in f:
        reg, instr, val, _, cond_reg, cond_type, cond_val = line.strip().split()
        condition = f'{registers[cond_reg]} {cond_type} {cond_val}'
        if eval(condition):
            registers[reg] += int(val) if instr == 'inc' else -int(val)
            max_reg = max(registers[reg], max_reg)

print(f'Part 1: {max(registers.values())}, Part 2: {max_reg}')
