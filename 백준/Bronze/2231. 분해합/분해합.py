import math
import heapq
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline


# 분해합이 들어오면 
# 그 분해합을 가지는 가장 작은 자연수를 출력하기 

if __name__ == "__main__":
    N = int(input())
    result = 0

    for i in range(N+1):
        decomposition_sum = i + sum(int(num) for num in str(i))

        if decomposition_sum == N:
            result = i
            break
    
    print(result)