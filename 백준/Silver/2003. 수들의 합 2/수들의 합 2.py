# N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다.
# 수열의 i번째 수부터 j번째 수까지의 합 A[i]+A[i+1]+…+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

count = 0
current_sum = 0
start = 0

for end in range(N):
    current_sum += A[end]  

    while current_sum > M and start <= end:
        current_sum -= A[start]  
        start += 1  

    if current_sum == M:
        count += 1  

print(count)