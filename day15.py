# Generator A starts with 883
# Generator B starts with 879

def generator(start, factor, n=1):
    while True:
        start = (start*factor)%2147483647
        if not start&(n-1): # Using bitwise and instead of modulos as it's slightly faster
            yield start & 0xffff

start_A, start_B = 883, 879
A, B = generator(start_A, 16807), generator(start_B, 48271), 
picky_A, picky_B = generator(start_A, 16807, 4), generator(start_B, 48271, 8)

matches = matches_picky = 0
for n in range(4*(10**7)):
    if next(A) == next(B):
        matches += 1
    if n < 5*(10**6) and next(picky_A) == next(picky_B):
        matches_picky += 1

print(f'Part 1: {matches}, Part 2: {matches_picky}')