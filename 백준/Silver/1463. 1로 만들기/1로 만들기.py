import math
from collections import deque
import sys
input = sys.stdin.readline


# 정수에 사용할 수 있는 연산은 다음 3가지임 
# 1. x가 3으로 나누어 떨어지면 3으로 나눔 
# 2. x가 2로 나누어 떨어지면, 2로 나눔 
# 3. 1을 뺌 
# 위 세 개의 연산을 사용해서 1을 만드는 최소 횟수 구하기 



if __name__ == "__main__":
    N = int(input())
    dp = [0] * (N+1)

    for i in range(2, N + 1):
        # 1을 빼는것은 항상 적용할 수있는 연산이다 
        # 그렇다면 일단 1을 배고 나누어 떨어지는지 확인해서 
        # min(dp[i], dp[i // 2 or 3] + 1)
        # 이런식으로 검사하면 N까지의 모든 dp 리스트가 완성됨 

        dp[i] = dp[i - 1] + 1

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)

        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    print(dp[N])

