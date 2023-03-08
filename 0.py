# https://www.acmicpc.net/problem/0

import sys

sys.setrecursionlimit(1_000_000)

n, k = map(int, sys.stdin.readline().split(' '))

arr = [list(map(int, sys.stdin.readline()[:-1].split(' '))) for _ in range(n)]

# ---

n, m = tuple(map(int, sys.stdin.readline().split(' ')))

arr = [list(map(int, list(sys.stdin.readline()[:-1]))) for _ in range(n)]
arr = [[0 for _ in range(m + 1)]] + list(map(lambda arr: [0] + arr, arr))
