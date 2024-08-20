# 준규가 가지는 동전은 N개의 종류이다.
# 각각의 동전은 매우 많이 가지고 있다.
# 그 가치의 합을 K로 만들려고 한다.

# 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

N, K = map(int, input().split())

coin = []
for i in range(N):
    coin.append(int(input()))

coin.sort(reverse=True)
result = 0

for i in coin:
    result += K // i
    K %= i

print(result)