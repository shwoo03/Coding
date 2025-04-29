import math
import sys
input = sys.stdin.readline


# 상근이가 N킬로그램을 배달해야 한다. 
# 3, 5 킬로그램 봉지가 있는데 가장 작은 개수의 봉투를 가지고 가려고 함 



if __name__ == "__main__":
    N = int(input())
    dp = [10000] * (N+1)
    dp[0] = 0

    # 3KG -> 5KG 봉투를 추가할 수 있는지의 순서로 작성해야 함 
    for i in range(1, N+1):
        if i >= 3:
            dp[i] = min(dp[i], dp[i-3] + 1)

        if i >= 5:
            dp[i] = min(dp[i], dp[i-5] + 1)
    
    if dp[N] == 10000:
        print(-1)
    else:
        print(dp[N])

