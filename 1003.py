# https://www.acmicpc.net/problem/1003


import sys


table = {
    0: [1, 0, 1] + ([0] * 38),
    1: [0, 1, 1] + ([0] * 41),
}


def f_base(base, n):
    t = table[base]

    if n > 40:
        return -1

    if n <= 2:
        return t[n]

    if t[n]:
        return t[n]

    for i in range(3, n + 1):
        if t[i]:
            continue
        t[i] = t[i - 2] + t[i - 1]

    return t[n]


def f0(n):
    return f_base(0, n)


def f1(n):
    return f_base(1, n)


t = int(sys.stdin.readline())

for _ in range(t):
    v = int(sys.stdin.readline())
    v0, v1 = f0(v), f1(v)
    print(v0, v1)
