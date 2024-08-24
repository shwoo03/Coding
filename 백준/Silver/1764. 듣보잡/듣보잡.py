# 모르는 사람의 명단이 주어질 때, 명단을 구하는 프로그램 작성
# N은 듣지 못한 사람의 수, M은 보지 못한 사람의 수

N, M = map(int, input().split())
list_N = []
list_M = []

for i in range(N):
    list_N.append(input())

for i in range(M):
    list_M.append(input())

result = list(set(list_N) & set(list_M))
result.sort()
print(len(result))
for i in result:
    print(i)