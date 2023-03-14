# https://www.acmicpc.net/problem/1011

import sys

sys.setrecursionlimit(1_000_000)


def compute(distance):

    x = 0
    y = 0
    while True:
        x += 1
        y += ((x + 1) // 2)
        if y >= distance:
            break

    return x


t = int(sys.stdin.readline())

results = [tuple(map(int, sys.stdin.readline()[:-1].split(' '))) for _ in range(t)]
results = [compute(y - x) for x, y in results]
[print(result) for result in results]


# APPENDIX

# x   y       inverse function:   x   y
# 0   0                           0   0
# 1   1                           1   1
# 2   2                           2   2
# 4   3                           3   4
# 6   4             ->            4   6
# 9   5                           5   9
# 12  6                           6   12
# 16  7                           7   16
# 20  7                           8   20
