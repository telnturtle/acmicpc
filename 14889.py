import sys
from typing import List


N = int(sys.stdin.readline())

S = []

for _ in range(N):
    S.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(i + 1, N):
        S[j][i] += S[i][j]

min_sum = 1000000


def case(p: List[bool], a_team: int, r: int) -> None:
    if r == len(p):
        pass
        return
    case(p.)
    
