from collections import deque
from functools import reduce
from operator import xor

with open('input.txt') as f:
    line = f.readline()
    lengths_1 = map(int, line.split(','))
    lengths_2 = list(map(ord, line)) + [17, 31, 73, 47, 23]

def reverse_slice(q, l):
    ns = []
    for _ in range(l):
        ns.append(q.popleft())
    for n in ns:
        q.appendleft(n)

def run(q, lengths, N=1):
    skip = overshoot = 0
    for _ in range(N):
        for l in lengths:
            reverse_slice(q, l)
            overshoot += l + skip
            q.rotate(-l-skip)
            skip += 1
    q.rotate(overshoot%256)

nums_1, nums_2 = deque(range(256)), deque(range(256))

run(nums_1, lengths_1)
run(nums_2, lengths_2, 64)

hash = ''.join(f'{reduce(xor, [nums_2.popleft() for _ in range(16)]):02x}' for _ in range(16))

print(f'Part 1: {nums_1.popleft() * nums_1.popleft()}, Part 2: {hash}')
