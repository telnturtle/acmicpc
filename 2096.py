# https://www.acmicpc.net/problem/2096

import sys


# input

N = int(sys.stdin.readline())

rows = ['000'] + [''.join(sys.stdin.readline().split(' ')) for _ in range(N)]

# DP

table_min = [[0, 0, 0], [0, 0, 0]]
table_max = [[0, 0, 0], [0, 0, 0]]

for i in range(1, N + 1):
    table_min[1][0] = int(rows[i][0]) + min(table_min[0][0], table_min[0][1])
    table_min[1][1] = int(rows[i][1]) + min(table_min[0][0], table_min[0][1], table_min[0][2])
    table_min[1][2] = int(rows[i][2]) + min(table_min[0][1], table_min[0][2])
    table_max[1][0] = int(rows[i][0]) + max(table_max[0][0], table_max[0][1])
    table_max[1][1] = int(rows[i][1]) + max(table_max[0][0], table_max[0][1], table_max[0][2])
    table_max[1][2] = int(rows[i][2]) + max(table_max[0][1], table_max[0][2])

    table_min[0][0] = table_min[1][0]
    table_min[0][1] = table_min[1][1]
    table_min[0][2] = table_min[1][2]
    table_max[0][0] = table_max[1][0]
    table_max[0][1] = table_max[1][1]
    table_max[0][2] = table_max[1][2]


# output

print(f'{max(table_max[1])} {min(table_min[1])}')
