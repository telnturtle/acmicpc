# https://www.acmicpc.net/problem/7576

import sys

sys.setrecursionlimit(1_000_000)

m, n = tuple(map(int, sys.stdin.readline().split(' ')))

arr = [list(map(int, list(sys.stdin.readline().split(' ')))) for _ in range(n)]
arr = [[-1 for _ in range(m + 2)]] + list(map(lambda arr: [-1] + arr + [-1], arr)) + [[-1 for _ in range(m + 2)]]


# def print_(arr):
#     for i in range(1, len(arr) - 1):
#         print(''.join([str(status) if status >= 0 else '_' for status in arr[i][1:-1]]))


unripes = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if arr[i][j] == 0:
            unripes += 1


border = set()
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if arr[i][j] == 1 and (
            arr[i-1][j] == 0 or arr[i+1][j] == 0 or arr[i][j-1] == 0 or arr[i][j+1] == 0
        ):
            border.add((i, j))


day = 0

while True:
    to_ripes = set()
    for i, j in border:
        for i_, j_ in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if arr[i_][j_] == 0:
                to_ripes.add((i_, j_))
                arr[i_][j_] = 1

    if len(to_ripes) == 0:
        break
    day += 1
    unripes -= len(to_ripes)
    border = to_ripes

print(day if unripes == 0 else -1)
