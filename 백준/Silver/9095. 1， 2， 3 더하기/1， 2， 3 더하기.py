# 정수가 주어지면 1,2,3의 합으로 구성할 수 있는 경우의 수를 구하는 프로그램 
# 마지막에 1, 2, 3인지 확인하여 dp[n]을 리턴하는 방식으로 해결 

n = int(input())
dp = [0] * 11
dp[0] = 1

for i in range(1, 11):
    dp[i] = dp[i - 1]

    if i >= 2:
        dp[i] += dp[i - 2]
    if i >= 3:
        dp[i] += dp[i - 3]

for _ in range(n):
    num = int(input())
    print(dp[num])