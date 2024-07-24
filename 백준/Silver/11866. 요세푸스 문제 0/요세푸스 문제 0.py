# 1 ~ N 번까지 N명의 사람이 원을 이루어서 앉아있고, 양의 정수 M(<= N)이 주어진다.
# 순서대로 k 번째 사람을 제고한다. 이 과정을 N명의 사람이 모두 제거될 때까지 계속한다.
# 원에서 사람들이 제거되는 순서를 (N, K)- 요세푸스 순열이라고 한다.
# N과 M이 주어지면 (N, K) 요세푸스 순열을 구하는 프로그램을 작성하시오.

N, K = map(int, input().split())
people = list(range(1, N+1))
result = []
index = 0

for i in range(N):
    index = (index + K - 1) % len(people)
    result.append(people.pop(index)) 

print("<" + ", ".join(map(str, result)) + ">")