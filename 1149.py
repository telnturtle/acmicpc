# https://www.acmicpc.net/problem/1149

import sys


N = int(sys.stdin.readline())

costs = [[0, 0, 0]] + [list(map(int, (sys.stdin.readline()).split(' '))) for _ in range(N)]

table = [[0, 0, 0] for _ in range(N + 1)]

for i in range(1, 1 + N):
    table[i][0] = min(table[i-1][1], table[i-1][2]) + costs[i][0]
    table[i][1] = min(table[i-1][0], table[i-1][2]) + costs[i][1]
    table[i][2] = min(table[i-1][0], table[i-1][1]) + costs[i][2]

# #
# # TEST: print
# #
# for i in range(N + 1):
#     print(f'{table[i][0]:4} {table[i][1]:4} {table[i][2]:4}')
# #
# #
# #

print(min(table[N]))
