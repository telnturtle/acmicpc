# https://www.acmicpc.net/problem/10844


# N      0      1      2      3      4      5      6      7      8      9
# -------------------------------------------------------------------------------
# 1      0      1      1      1      1      1      1      1      1      1
# 2      1      1      2      2      2      2      2      2      2      2
# Ex.    10     21     12 32  23 43  34 54  45 65  ...           78 98  89
# 3      1      3      3      4      4      4      4      4      4      2
# sentinel
# None
# def:
# d belongs to [0, 9]
# S(n, d) = number of stairnum
#   where number of digits equals to `n` and digits ends with `d`
# S(n, d) = [if n = 0 then 0 else 1] where n = 1
# S(n, d) = [
#   if n = 0 then S(n-1, 1) else
#       if n = 9 then S(n-1, 8) else
#           S(n-1, d-1) + S(n-1, d+1)]
#   where n > 1
#
# def:
# S(n) = sum({ S(n, d) | d belongs to [0, 9] })


def S(n, T):
    # T is 1x10 table
    # iterate N-1 times to compute answer
    while n > 1:
        # n <- n...1
        next = [0 for _ in range(10)]
        # array for next T
        next[0] = T[1]
        for i in range(1, 9):
            # i <- 1...8
            next[i] = T[i-1] + T[i+1]
        next[9] = T[8]
        # compute next T
        for i in range(len(T)):
            T[i] = next[i]
        # rewrite next T
        n -= 1


def solve(n, table):
    S(n, table)
    return sum(table)


if __name__ == '__main__':
    import sys

    N = int(sys.stdin.readline())
    table = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # initiate the table

    number_of_stairnums = solve(N, table)

    print(number_of_stairnums % 1_000_000_000)
