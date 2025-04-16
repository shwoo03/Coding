import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# RGB 거리에는 N개의 집이 있음 
# 거리는 선분으로 나타낼 수 있고, 1 ~ N 집이 순서대로 존재함 
# 빨, 초, 파 중 하나로 칠해야 한다.
# 각 색의 비용이 주어졌을 때 아래 규칙을 만족하면서 모든 집을 칠하는 최소 비용 구하기

# 1. 1번 집의 색은 2번 집의 색과 같지 않아야 함.
# 2. N번 집의 색은 N-1번 집의 색과 같지 않아야 함.
# 3. i(2 <= i <= N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 함.


# DP로 풀 수 있을듯함.
# dp[i][j] = i번째 집을 j색으로 칠했을 때 최소 비용 




if __name__ == "__main__":
    N = int(input())
    cost = [None] + [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * 3 for _ in range(N+1)]

    dp[1][0] = cost[1][0] # 빨 
    dp[1][1] = cost[1][1] # 초
    dp[1][2] = cost[1][2] # 파 

    for i in range(2, N+1):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0] # 빨간색 + min(초, 파)
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1] # 초록색 + min(빨, 파)
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2] # 파란색 + min(빨, 초)

    print(min(dp[N]))


# 25 40 83
# 49 60 57
# 13 89 99

# dp = [26, 40, 83]
# dp = [89, 86, 83]
# dp = [96, 172, 185]