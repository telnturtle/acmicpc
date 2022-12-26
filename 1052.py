# https://www.acmicpc.net/problem/1052

n, k = map(int, (input()).split(' '))

# IDEA : N + x를 K개의 2의 제곱수들의 합으로 바꾸는 데, 필요한 가장 작은 x는?


def largest_power_of_two(n: int) -> int:
    i = 0
    while n >= 2:
        n /= 2
        i += 1
    return 2**i


purchase = 0
last_lpt = 0
for _ in range(k):
    if n <= 0:
        break
    lpt = largest_power_of_two(n)
    last_lpt = lpt
    n -= lpt
if n > 0:
    purchase = last_lpt - n

print(purchase)
