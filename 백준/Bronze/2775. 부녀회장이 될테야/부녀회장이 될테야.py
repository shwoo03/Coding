import math
import sys
input = sys.stdin.readline


# a층 b호에 살려면 자신의 a-1층 부터 b호까지 사람들의 수의 합만큼 사람들을 데려와야 함 
# 몇명인지 구하는 코드 작성 


if __name__ == "__main__":
    T = int(input())
    dp = [[0] * 15 for _ in range(15)]

    # 테이블 채우기 
    # 1,3 들어오면 -> 0층 [1,2,3,4, 5, 6, 7, 8,9,10,11,12,13,14]
    #              -> 1층 [1,3,6,10,15,21,28,36, ..... ]
    # dp[i] = dp[floor-1][bang] + dp[floor][bang-1]
    for i in range(1, 15):
        dp[0][i] = i
    

    for floor in range(1, 15):
        for bang in range(1, 15):
            dp[floor][bang] = dp[floor-1][bang] + dp[floor][bang-1]
    
    for i in range(T):
        floor = int(input())
        bang = int(input())
        print(dp[floor][bang])

