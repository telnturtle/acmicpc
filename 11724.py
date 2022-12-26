import sys


n, m = map(int, sys.stdin.readline().split())
sets = [None] * (m + 1)
# Initialize sets
for i in range(1, len(sets)):
    sets[i] = set()
for _ in range(n):
    u, v = sys.stdin.readline().split()
    sets[u]
