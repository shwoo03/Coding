# 양의 정수 n개가 주어졌을 때, 가능한 모든 쌍의 GCD의 합을 구하는 프로그램을 작성하시오.

N = int(input())

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

for _ in range(N):
    data = list(map(int, input().split()))
    result = 0
    for i in range(1, len(data)):
        for j in range(i+1, len(data)):
            result += gcd(data[i], data[j])
    print(result)

