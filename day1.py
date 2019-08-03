with open('input.txt') as f:
    captcha = list(map(int, f.readline().strip()))

sum1 = sum2 = 0
N = len(captcha)//2
for i, c in enumerate(captcha):
    sum1 += c if captcha[i-1] == c else 0
    sum2 += c if captcha[i-N] == c else 0

print(f'Part 1: {sum1}, Part 2: {sum2}')