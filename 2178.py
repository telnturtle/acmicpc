# https://www.acmicpc.net/problem/2178

import sys

sys.setrecursionlimit(1_000_000)

n, m = tuple(map(int, sys.stdin.readline().split(' ')))

arr = [list(map(int, list(sys.stdin.readline()[:-1]))) for _ in range(n)]
arr = [[0 for _ in range(m + 1)]] + list(map(lambda arr: [0] + arr, arr))

table = [[0 for __ in range(m + 1)] for _ in range(n + 1)]
table[1][1] = 1

queue = [(1, 1)]

while len(queue):
    x, y = queue.pop(0)
    candidates = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    for x_, y_ in candidates:
        if x_ <= m and y_ <= n and arr[y_][x_] and not table[y_][x_]:
            table[y_][x_] = table[y][x] + 1
            queue.append((x_, y_))
    if table[n][m]:
        break

print(table[n][m])
exit()
