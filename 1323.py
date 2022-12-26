import math


def main(n, k):
    # 홀짝
    if n % 2 == 1 and k % 2 == 0:
        return -1

    # 5의 배수
    if (n % 5 != 0) and (k % 5 == 0):
        return -1

    # 10의 배수
    if (n % 5 == 0):
        digits = int(math.log10(n)) + 1
        hold = n

        for i in range(1, 12):
            if hold % k == 0:
                return i
            hold = hold * 10**digits + n

        return -1

    # k가 2의 power, >= 4, n이 짝수고 끝자리가 2, 6, 0일 때
    if (math.log2(k) == int(math.log2(k)) and k >= 4 and n % 2 == 0 and n % 10 in [2, 6, 0]):
        return -1

    # 나눠지는 경우
    digits = int(math.log10(n)) + 1
    hold = n

    for i in range(1, 1000):
        if hold % k == 0:
            return i
        hold = hold * 10**digits + n

    return -1

# f(n, m): 
# assert main(10, 4) == -1, '10, 4 -> -1'
# assert main(6, 4) == -1, '6, 4 -> -1'
# assert main(2, 9) == 9, '2, 9 -> 9'
# assert main(23984, 182) == 6

n, k = list(map(int, input().split()))
print(main(n, k))
