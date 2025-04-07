import sys
input = sys.stdin.readline


# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열의 길이를 구하는 문제

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    # n 번째 수열의 길이를 dp[n]이라고 하면 
    # dp[n] = max(dp[i]) + 1 (i < n and a[i] < a[n])
    # dp[0] = 1 (첫 번째 수열은 항상 1)
    # dp[1] = 2 (첫 번째 수열과 두 번째 수열이 증가하는 경우)
    # dp[2] = 3 (첫 번째 수열과 두 번째 수열과 세 번째 수열이 증가하는 경우)
    # dp[3] = 4 (첫 번째 수열과 두 번째 수열과 세 번째 수열과 네 번째 수열이 증가하는 경우)

    dp = [1] * n

    for i in range(1,n):
        for j in range(i):
            if a[i] > a[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    print(max(dp))




