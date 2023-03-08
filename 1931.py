# https://www.acmicpc.net/problem/1931

import sys

sys.setrecursionlimit(1_000_000)

n = int(sys.stdin.readline())

arr = [tuple(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]
arr = list(map(lambda x: (x[1], x[0]), arr))

arr.sort()

i = 0
until = 0
meetings = 0

while len(arr) > i:
    if arr[i][1] >= until:
        until = arr[i][0]
        i += 1
        meetings += 1
    else:
        i += 1

print(meetings)
