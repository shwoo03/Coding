import math
import sys
input = sys.stdin.readline



# 2 x n 직사각형을 1x2, 2x1 타일로 채우는 방법의 수를 구하는 프로그램 작성하기 
# 2 x n 직사각형을 채우는 수의 리스트를 dp[i] 라고 해보면 
# dp[1] = 1 이다.
# dp[2] = 2 이다.
# dp[3] = 3 -> dp[1] + dp[2]
# dp[4] = 5 -> dp[2] + dp[3]
# dp[i] = dp[i-1] + dp[i-2] 이다. 결국 2x1 또는 1x2 이므로
# 이미 완성된 퍼즐에서 붙일 수 있는 수가  i-1, i-2에서의 타일 밖에 없으므로 점화식은 위와 같음 


if __name__ == "__main__":
    n = int(input())
    dp = [0] * 1001
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 10007
    
    print(dp[n])