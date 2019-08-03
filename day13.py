with open('input.txt') as f:
    scanners = [tuple(map(int, l.split(': '))) for l in f]

def caught_severities(scanners, delay=0):
    return [r*d for r, d in scanners if (r+delay)%(2*d-2) == 0]

delay = 1 # Takes a while, not sure howto do analytically
while len(caught_severities(scanners, delay)):
    print(delay)
    delay += 1

print(f'Part 1: {sum(caught_severities(scanners))}, Part 2: {delay}')