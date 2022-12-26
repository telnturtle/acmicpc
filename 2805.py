n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()
max_height = trees[-1]


_up_index = 0
_up = trees[_up_index]
up = [(0, n)]
_n = n
for i in range(1, max_height + 1):
    if i > _up:
        while i > _up:
            _up_index += 1
            _up = trees[_up_index]
            _n -= 1
        up.append((i, _n))


# h(0 -> max) : amount
chopped = sum(trees)
up_index = 0
for i in range(1, max_height + 1):
    if up_index != len(up) - 1:
        if i == up[up_index + 1][0]:
            up_index += 1
    chopped -= up[up_index][1]
    if chopped < m:
        print(i - 1)
        break
