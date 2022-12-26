# https://www.acmicpc.net/problem/1966

import sys
from dataclasses import dataclass


# struct


@dataclass
class TC():
    N: int
    index: int
    priorities: list[int]


# input


testcases = []

for _ in range(int(sys.stdin.readline())):
    [N, index] = list(map(int, sys.stdin.readline().split(' ')))
    priorities = list(map(int, sys.stdin.readline().split(' ')))
    docs = TC(N, index, priorities)
    testcases.append(docs)


def compute(tc: TC) -> int:
    result = tc.N
    highers = len(list(filter(lambda x: x > tc.priorities[index], tc.priorities)))
    result -= highers
    
    
    return 0
