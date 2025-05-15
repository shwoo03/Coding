import math
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


# 수열 A가 주어지면 가장 긴 증가하는 부분 수열을 구하는 문제
# [1,1,1,1,1,1,1,1,1,1....] 일 때, 증가하는 부분들에서
# 모든 경우의 수를 고려해야 하기 때문에 1,2,3 번째 요소들의 
# 최대 수열의 길이를 고려해야 함 따라서 모든 요소를 순회해야 함 
#   증가하는 부분 수열이기 때문에 수가 증가해야 하므로 
#   2중 for문을 사용하여 max 값을 정해놓고 0번 index부터 증가하면서 비교하면 됨  
# 만약, if list_num[j] < list_num[i] 가 되면 자신보다 작은 수가 존재하므로 해당 index에서 
#   dp[i] = max[dp[i], dp[j] + 1] 이렇게 하면 됨 

if __name__ == "__main__":
    T = int(input())
    list_num = list(map(int, input().split()))

    dp = [1] * T

    for i in range(T):
        for j in range(i):
            if list_num[j] < list_num[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    print(max(dp))