from collections import deque

step_size = 377

buffer = deque([0])

for i in range(1, 2018):
    buffer.rotate(-step_size-1)
    buffer.appendleft(i)

val = current_pos = 0
for i in range(1, 50000001):
    current_pos = (current_pos+step_size)%i + 1
    if current_pos == 1:
        val = i

print(f'Part 1: {buffer[1]}, Part 2: {val}')