# https://www.acmicpc.net/problem/1043

import sys

sys.setrecursionlimit(1_000_000)

readline = sys.stdin.readline

n, m = tuple(map(int, readline().split(' ')))

truth_people = list(map(int, readline()[:-1].split(' ')))[1:]
truth_people = set(truth_people)

people_per_party = [set(list(map(int, readline()[:-1].split(' ')))[1:]) for _ in range(m)]


network = {i: set() for i in range(1, n + 1)}
for party_people in people_per_party:
    for person in party_people:
        network[person] = network[person].union(party_people)
for person in range(1, n + 1):
    if person in network[person]:
        network[person].remove(person)


truth_network = set()
queue = list(truth_people)
while len(queue):
    person = queue.pop(0)
    if person not in truth_network:
        truth_network.add(person)
        for node in network[person]:
            if node not in truth_network:
                queue.append(node)


print(len(list(filter(truth_network.isdisjoint, people_per_party))))
