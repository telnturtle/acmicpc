# https://www.acmicpc.net/problem/1032
import sys

n = int(sys.stdin.readline())

strings = []
for i in range(n):
    strings.append(sys.stdin.readline())

pattern = list(strings[0])

for s in strings[1:]:
    for i in range(len(s)):
        match = s[i] == pattern[i]
        if not match:
            pattern[i] = '?'

pattern = ''.join(pattern)

print(pattern)
