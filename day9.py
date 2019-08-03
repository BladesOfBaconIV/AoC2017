with open('input.txt') as f:
    stream = f.readline().strip()

depth = in_gargbage = ignore = 0
score = garbage_score = 0
for c in stream:
    if in_gargbage:
        if ignore:
            ignore = 0
        elif c == '!':
            ignore = 1
        elif c == '>':
            in_gargbage = 0
        else:
            garbage_score += 1
    else:
        if c == '<':
            in_gargbage = 1
        elif c == '{':
            depth += 1
        elif c == '}':
            score += depth
            depth -= 1

print(f'Part 1: {score}, Part 2: {garbage_score}')