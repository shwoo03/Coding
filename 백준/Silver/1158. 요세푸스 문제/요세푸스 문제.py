# 1부터 N까지의 N명으 사람이 원을 이루면서 앉아있고, 양의 정수 K가 주어진다.
# 순서대로 K번째 사람을 제거한다. 이 과정을 반복하여 한 명이 남을 때까지 계속한다.

# N, K가 주어지면 요세푸스 순열을 출력하는 프로그램을 작성하시오.

N, K = map(int, input().split())
people = [i for i in range(1, N+1)]
result = []

while people:
    for i in range(K-1):
        people.append(people.pop(0))
    result.append(people.pop(0))

print('<', end='')
print(*result, sep=', ', end='')
print('>')
