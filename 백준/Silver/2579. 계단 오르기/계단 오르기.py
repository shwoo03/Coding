import math
from collections import deque
import sys
input = sys.stdin.readline


# 1. 한 번에 한 계단 또는 두 계단씩 오를 수 있음 
# 2. 한 계단을 밟으면서 이어서 다음 계단이나 다음다음 계단으로 오를 수 있음 
# 3. 마지막 계단은 무조건 밟아야 함 
# 얻을 수 있는 점수의 최대값을 구하는 프로그램을 작성
# 두 칸씩 올라가는 식은 dp[i-2] + list_score[i] 이런식으로 가능하다 
# 한칸 씩 올라가지만 연속 세 번은 못하는 것은 다음과 같이 표현이 가능할 것이다 
#     dp[i-3] + list_score[i-1] + list_score[i] -> i-3 까지는 오고 i-2를 건너뛰고 2개를 밟으면 된다 
# max(dp[i-2] + list_score[i], dp[i-3] + list_score[i-1] + list_score[i])


if __name__ == "__main__":
    N = int(input())
    list_score = [int(input()) for _ in range(N)]

    dp = [0] * (N)

    if N == 1:
        print(list_score[0])
    elif N == 2:
        print(list_score[0] + list_score[1])
    else:
        dp[0] = list_score[0]
        dp[1] = list_score[0] + list_score[1]
        dp[2] = max(list_score[0] + list_score[2], list_score[1] + list_score[2])

        for i in range(3, N):
            dp[i] = max(dp[i-2] + list_score[i], dp[i-3] + list_score[i-1] + list_score[i])
        
        print(dp[N-1])