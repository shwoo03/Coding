import math
import heapq
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline


# 이항 계수를 구하려면 N! / K!(N-K)! 이다.


if __name__ == "__main__":
    N, K = map(int, input().split())

    son = 1
    for i in range(1, N+1):
        son *= i
    
    mom = 1
    N_K = N - K
    for i in range(1, N_K+1):
        mom *= i
    
    for i in range(1, K+1):
        mom *= i
    
    print(son // mom)
