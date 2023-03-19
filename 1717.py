# https://www.acmicpc.net/problem/1717

import sys

sys.setrecursionlimit(1_000_000)

# ---


n, m = tuple(map(int, sys.stdin.readline()[:-1].split(' ')))

parent = list(range(n + 1))
insts = [list(map(int, list(sys.stdin.readline()[:-1].split(' ')))) for _ in range(m)]


def union(a, b):
    if a == b:
        return

    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        if root_a > root_b:
            parent[root_a] = root_b
        else:
            parent[root_b] = root_a


def find(i):
    node = i
    while True:
        if parent[node] == node:
            return node
        node = parent[node]


def check_same(a, b):
    if a == b:
        return True
    return find(a) == find(b)


for inst in insts:
    op, a, b = inst

    if op == 0:
        union(a, b)
    else:
        result = 'yes' if check_same(a, b) else 'no'
        print(result)
