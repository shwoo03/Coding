# 2xn 크기의 직사각형을 1x2, 2x1 타일로 채우는 경우의 수를 구하는 문제

# 접근 
# n이 1이면 1, 
# n이 2면 2,
# n이 3이면 3,
# n이 4면 5,
# n이 5면 8,
# 점화식은 dp[i] = dp[i - 1] + dp[i - 2]로 나타낼 수 있다.

n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[n] % 10007)