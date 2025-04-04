import sys
input = sys.stdin.readline


# N개가 주어지면 i 부터 j까지의 합을 구하는 문제

N, M = map(int, input().split())
num_list = list(map(int, input().split()))

# 누적합을 통해 문제를 해결해야 함 
# 그냥 for문으로 돌리면 시간초과 남 
sum_list = [0] * (N + 1)
for i in range(1, N + 1):
    sum_list[i] = sum_list[i - 1] + num_list[i - 1]


for _ in range(M):
    a, b = map(int, input().split())
    print(sum_list[b] - sum_list[a - 1])
