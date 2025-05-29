import math
import heapq
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline


# 일렬로 놓여져 있는 포도주를 다음 규칙으로 먹음 
#   1. 마시고 원래 위치에 돌려 놓는다 
#   2. 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.
# 포도주 양이 주어졌을 때 가장 많이 마실 수 있는 양을 구하는 프로그램 작성
# DP 문제인듯 
#   경우의 수는 3가지다 dp[i]는 다음과 같이 결정된다. 
#   1. 안 마시기 -> dp[i-1]
#   2. 이번 잔만 마시기 -> dp[i-2] + wine[i]
#   3. 이전 잔 마시고, 이번 잔도 마시기 -> dp[i-3] + wine[i-1] + wine[i]
#   이러면 연속 3잔을 안마시게 하는 안전장치가 존재

if __name__ == "__main__":
    N = int(input())
    wine = []
    for i in range(N):
        wine.append(int(input()))
    
    if N == 1:
        print(wine[0])
    elif N == 2:
        print(wine[0] + wine[1])
    else:
        dp = [0] * N
        dp[0] = wine[0]
        dp[1] = wine[0] + wine[1]
        dp[2] = max(wine[0] + wine[2] , wine[1] + wine[2], dp[1])

        for i in range(3, N):
            dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])
        
        print(dp[N-1])



