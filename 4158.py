import sys


while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    sanggeun = set()
    for i in range(n):
        sanggeun.add(int(sys.stdin.readline()))
    count = 0
    for i in range(m):
        if int(sys.stdin.readline()) in sanggeun:
            count += 1
    print(count)
