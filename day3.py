from math import ceil

N = 325489

square_size = ceil(N**0.5)
square_size += (square_size+1)%2

dist_to_centre = square_size//2

layer_start = (square_size-2)**2 + 1

#calc midpionts around layer
m1 = layer_start + dist_to_centre - 1
mids = m1, m1 + 2*dist_to_centre, m1 + 4*dist_to_centre, m1 + 6*dist_to_centre

dist_to_mid = min(abs(N-m) for m in mids)

print(f'Part 1: {dist_to_centre+dist_to_mid}')

# Part 2 was found on https://oeis.org/A141481, ans = 330785