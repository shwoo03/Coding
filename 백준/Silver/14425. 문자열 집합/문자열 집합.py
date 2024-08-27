# 총 N개의 문자열로 이뤄진 집합 S가 있다.
# 입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되는 것이 총 몇 개인지 확인하는 프로그램 작성 

N, M = map(int, input().split())

S = set()
for _ in range(N):
    S.add(input())

count = 0

for _ in range(M):
    if input() in S:
        count += 1

print(count)