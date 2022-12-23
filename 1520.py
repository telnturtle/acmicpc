# https://www.acmicpc.net/problem/1520


import sys

sys.setrecursionlimit(1_000_000)

# input


M, N = tuple(map(int, (sys.stdin.readline()).split(' ')))

m = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(M)]

# backtracking and memoization

table = [[0 for _ in range(N)] for _ in range(M)]
touched = [[False for _ in range(N)] for _ in range(M)]


def f(i, j):
    if (i+1, j+1) == (M, N):
        return 1

    if touched[i][j]:
        return table[i][j]
    touched[i][j] = True

    inext, jnext = i-1, j
    if 0 <= inext < M and 0 <= jnext < N and m[i][j] > m[inext][jnext]:
        table[i][j] += f(inext, jnext)
    inext, jnext = i+1, j
    if 0 <= inext < M and 0 <= jnext < N and m[i][j] > m[inext][jnext]:
        table[i][j] += f(inext, jnext)
    inext, jnext = i, j-1
    if 0 <= inext < M and 0 <= jnext < N and m[i][j] > m[inext][jnext]:
        table[i][j] += f(inext, jnext)
    inext, jnext = i, j+1
    if 0 <= inext < M and 0 <= jnext < N and m[i][j] > m[inext][jnext]:
        table[i][j] += f(inext, jnext)
    return table[i][j]


f(0, 0)

# # test output

# for i in table:
#     print(i)

# output

print(table[0][0])
