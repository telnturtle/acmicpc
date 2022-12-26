n, _ = map(int, input().split())
seq = list(map(lambda x: int(x) - 1, input().split()))
count = 0
l = len(seq)
for i in range(l):
    pos = seq[i]
    length = n - i
    left = pos - 0
    right = length - pos
    if left < right:
        for j in range(i, l):
            seq[j] = (seq[j] - left - 1) % length
        count += left
    else:
        for j in range(i, l):
            seq[j] = (seq[j] + right - 1) % length
        count += right
print(count)
