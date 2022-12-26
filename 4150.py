n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    prev, curr = 1, 1
    for _ in range(n - 2):
        temp = curr
        curr += prev
        prev = temp
    print(curr)
