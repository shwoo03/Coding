N, M = map(int, input().split())

set_N = set()
for i in range(N):
    set_N.add(input())

set_M = set()
for i in range(M):
    set_M.add(input())

# 교집합 구하기
answer_set = set_N & set_M
answer_list = sorted(answer_set)

print(len(answer_list))
for i in answer_list:
    print(i)