# https://www.acmicpc.net/problem/1107

import sys

sys.setrecursionlimit(1_000_000)


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
if m == 0:
    brokens = set()
else:
    brokens = set(sys.stdin.readline()[:-1])  # set of one-length strings
dumb = abs(n - 100)
if m == 10:
    print(dumb)
    exit()

result = dumb

for channel in range(1_000_001):
    if set(str(channel)).isdisjoint(brokens):
        diff = abs(channel - n)
        channel_length = len(str(channel))
        result = min(channel_length + diff, result)

print(result)
