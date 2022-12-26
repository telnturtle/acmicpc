# https://www.acmicpc.net/problem/11053


# sentinel
# max({empty set}) = 0, arr[0] = -infinity
# def:
# LIS(i): LIS of arr[i...n], begins with arr[i].
# recursive def:
# LIS(i) = 1 + max({ LIS(j) | arr[i] < arr[j], i < j })


import sys


def maxproxy(list_):
    return max(list_) if len(list_) > 0 else 0


def LIS(A, N, T):
    T[N] = 1
    for i in range(N-1, -1, -1):
        # i <- n-1...0
        ds = [T[j] for j in range(i+1, N+1) if A[i] < A[j] and T[i] < T[j]+1]
        T[i] = 1 + maxproxy(ds)


def solve(arr, N, table):
    LIS(arr, N, table)
    return table[0] - 1


if __name__ == '__main__':
    import sys

    N = int(sys.stdin.readline())
    sentinel = 0
    # 1 ≤ Ai ≤ 1,000
    arr = [sentinel] + list(map(int, sys.stdin.readline().split(' ')))
    table = [1 for _ in range(N+1)]
    # initiate the table

    length = solve(arr, N, table)

    print(length)
