# https://www.acmicpc.net/problem/1697

from collections import defaultdict
import sys

n, k = map(int, sys.stdin.readline().split(' '))


queue = [n]
visited = set()
distance = defaultdict(int)


while len(queue):
    x = queue.pop(0)
    if x == k:
        break
    for pivot in [x - 1, x + 1, 2 * x]:
        if (pivot not in visited) and (0 <= pivot <= 100_000):
            visited.add(pivot)
            queue.append(pivot)
            distance[pivot] = distance[x] + 1


print(distance[k])
