# https://www.acmicpc.net/problem/12865


import sys


n, k = tuple(map(int, sys.stdin.readline().split(' ')))


stuffs = [[0, 0]] + [[int(x) for x in list(sys.stdin.readline()[:-1].split(' '))] for _ in range(n)]

# vertical length (n+1) by horizontal length (k+1) table
table = [[0 for _ in range(k + 1)] for __ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        stuffs[i][0]
        stuffs[i][1]

        if j >= stuffs[i][0]:
            table[i][j] = max(table[i - 1][j], table[i - 1][j - stuffs[i][0]] + stuffs[i][1])
        else:
            table[i][j] = table[i - 1][j]
        # 점화식:
        #       {
        #           table[i][j] = max(table[i-1][j], table[i-1][j-w_i]+v_i) ,  j-w_i > 0
        #           table[i][j] = table[i-1][j]                             ,  j-w_i < 0
        #       }

# 시간복잡도 O(n . k)

print(table[n][k])
