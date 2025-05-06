import math
import sys
input = sys.stdin.readline



# 정수가 입력되면 n을 1,2,3의 합으로 나타내는 방법의 수를 출력하기 
# 그렇다면 n-3 까지의 경우의 수 + 1,2,3 의 경우의 수를 모두 구하면 되므로 
# 1 -> 1
# 2 -> 11, 2
# 3 -> 111, 112, 121, 211
# 4 -> 13, 31, 112, 121, ..........
# dp[i] = dp[i-1] + dp[i-2] + dp[i-3] 이다.


if __name__ == "__main__":
    T = int(input())

    dp = [0] * 10000
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, 12):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    for i in range(T):
        print(dp[int(input())])

