from collections import deque
from functools import reduce
from operator import xor

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


def knot_hash(input):
    nums = deque(range(256))
    ls = list(map(ord, input)) + [17, 31, 73, 47, 23]
    run(nums, ls, 64)
    return ''.join(f'{reduce(xor, [nums.popleft() for _ in range(16)]):02x}' for _ in range(16))


def main():
    with open('input.txt') as f:
        line = f.readline()
        lengths_1 = map(int, line.split(','))

    nums_1 = deque(range(256))
    run(nums_1, lengths_1)
    
    print(f'Part 1: {nums_1.popleft() * nums_1.popleft()}, Part 2: {knot_hash(line)}')

if __name__ == '__main__':
    main()
