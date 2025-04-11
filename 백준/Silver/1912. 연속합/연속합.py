import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# n개 정수로 이루어진 임의 수열이 주어짐 
# 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 함 
# 단, 수는 한 개 이상 선택해야 함 




if __name__ == "__main__":
    n = int(input())
    num_list = list(map(int, input().split()))

    # 판단 기준은 2가지이다.
    # 1. 현재 수가 다음 수를 더한 것보다 크면 현재 수를 선택한다. (즉, 새로 시작하는 것)
    # 2. 현재 수가 다음 수를 더한 것보다 작으면 다음 수를 선택한다. (즉, 계속 이어서 더하는 것)
    dp = [0] * n
    dp[0] = num_list[0]

    for i in range(1, n):
        dp[i] = max(num_list[i], dp[i-1] + num_list[i])

print(max(dp))