import math
import heapq
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline


# 1 ~ N개의 집의 지붕을 빨, 초, 파 중에 하나로 색칠해야함 
# 각 색의 비용지 주어졌을 때 아래 규칙을 만족하는 최솟값을 구하기 
#   1번 집의 색은 2번 집의 색과 같지 않아야 한다.
#   N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
#   i번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다. 
# 즉, 이웃한 집의 색은 서로 달라야 한다. 
#   그렇다면 각 집을 3가지 색으로 칠했을 때의 모든 비용을 dp 배열에 저장하고 
#   그 중에서 min 함수를 사용해서 가장 낮은 비용을 가진 값과 더하면 된다. 


if __name__ == "__main__":
    house_num = int(input())
    list_cost = []
    for i in range(house_num):
        list_cost.append(list(map(int, input().split())))

    dp = [[0] * 3 for i in range(house_num)]
    dp[0][0] = list_cost[0][0]
    dp[0][1] = list_cost[0][1]
    dp[0][2] = list_cost[0][2]

    for i in range(1, house_num):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + list_cost[i][0] # 전 색이 빨 - 그렇다면 min(초,파) + 이전 cost 
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + list_cost[i][1] # 전 색이 초 - 그렇다면 min(빨,파) + 이전 cost
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + list_cost[i][2] # 전 색이 파 - 그렇다면 min(빨,초) + 이전 cost 

    print(min(dp[house_num-1]))