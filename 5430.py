# https://www.acmicpc.net/problem/5430

import sys

sys.setrecursionlimit(1_000_000)


def process():
    p = sys.stdin.readline()[:-1]
    n = int(sys.stdin.readline())
    if n == 0:
        sys.stdin.readline()
        arr = []
    else:
        arr = sys.stdin.readline()[1:-2].split(',')

    is_reversed = False

    for j in range(len(p)):
        if p[j] == 'R':
            is_reversed = not is_reversed
        else:
            if len(arr) == 0:
                return 'error'
            if is_reversed:
                arr.pop()
            else:
                arr.pop(0)

    if is_reversed:
        arr.reverse()

    arr = map(str, arr)

    return f"[{','.join(arr)}]"


t = int(sys.stdin.readline())

results = []

for i in range(t):
    result = process()
    results.append(result)

for result in results:
    print(result)
