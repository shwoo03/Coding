import math
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline


# n개의 정수로 이루어진 수열이 주어짐 
# 여기서 선택을 통해 최대 합을 구하려고 함 
# 단, 수는 한 개 이상 선택해야 함 
#   max 값을 정해놓고 i번째 까지의 + arr[i] 가 현재 배열의 arr[i] 값보다 작다면?
#   max 값을 arr[i]로 바꿔야 다시 최대 값을 찾을 수 있을 것이다.
#   즉, 점화식은 dp[i] = max(dp[i-1] + arr[i], arr[i])




if __name__ == "__main__":
    N = int(input())
    list_num = list(map(int, input().split()))
    dp = [0] * N
    dp[0] = list_num[0]

    for i in range(1, N):
        dp[i] = max(dp[i-1] + list_num[i], list_num[i])
        
    
    print(max(dp))

