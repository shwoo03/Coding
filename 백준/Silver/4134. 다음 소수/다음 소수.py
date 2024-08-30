# 정수 n이 주어지면, n보다 크거나 같은 소수 중 가장 작은 소수 찾는 프로그램 작성

T = int(input())

for j in range(T):
    n = int(input())
    i = n
    while True:
        is_prime = True
        if i < 2:
            is_prime = False
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            break
        i += 1

    print(i)