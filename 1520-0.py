# https://www.acmicpc.net/problem/1520


import sys


M, N = tuple(map(int, (sys.stdin.readline()).split(' ')))

m = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(M)]

m1 = [[0 for _ in range(N)] for _ in range(M)]

m2 = [[0 for _ in range(N)] for _ in range(M)]

m3 = [[0 for _ in range(N)] for _ in range(M)]

# make map 1

m1[0][0] = 1

for i in range(1, M):
    ltu = m[i-1][0] > m[i][0]
    m1[i][0] = m1[i-1][0] if ltu else 0
for j in range(1, N):
    ltl = m[0][j-1] > m[0][j]
    m1[0][j] = m1[0][j-1] if ltl else 0
for i in range(1, M):
    for j in range(1, N):
        m1[i][j] = 0
        ltu = m[i-1][j] > m[i][j]
        ltl = m[i][j-1] > m[i][j]
        m1[i][j] += m1[i-1][j] if ltu else 0
        m1[i][j] += m1[i][j-1] if ltl else 0

# make map 2

m2[M-1][N-1] = 0

for i in range(0, M-1):
    for j in range(0, N-1):
        m2[i][j] = 0
        ltd = m[i+1][j] > m[i][j]
        ltr = m[i][j+1] > m[i][j]
        m2[i][j] += m1[i+1][j] if ltd else 0
        m2[i][j] += m1[i][j+1] if ltr else 0
for i in range(0, M-1):
    ltd = m[i+1][N-1] > m[i][N-1]
    m2[i][N-1] = m1[i+1][N-1] if ltd else 0
for j in range(0, N-1):
    ltr = m[M-1][j+1] > m[M-1][j]
    m2[M-1][j] = m1[M-1][j-1] if ltr else 0

# make map 3

for i in range(0, M):
    m3[i][0] = m1[i][0] + m2[i][0]
for j in range(1, N):
    m3[0][j] = m1[0][j] + m2[0][j]
for i in range(1, M):
    for j in range(1, N):
        m12sum = m1[i][j] + m2[i][j]
        ltu = m[i-1][j] > m[i][j]
        ltl = m[i][j-1] > m[i][j]
        maybe_m3 = 0
        maybe_m3 += m3[i-1][j] if ltu else 0
        maybe_m3 += m3[i][j-1] if ltl else 0
        m3[i][j] = max(m12sum, maybe_m3)

# test output

for i in range(M):
    for j in range(N):
        print((m1[i][j], m2[i][j], m3[i][j]), end=' ')
    print()

# output

print(m3[M-1][N-1])
