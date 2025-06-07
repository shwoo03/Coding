import math
import heapq
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline


# 벌집        방 개수 
# 1 = 1         1
# 2~7 = 2       6
# 8~19 = 3      12
# 20~37 = 4     18
# 38~61 = 5     24
#   즉 층 수는 -> 1 + 3 * (층수 - 1) * 층수에 따라서 올라감 

if __name__ == "__main__":
    N = int(input())
    floor = 1
    max_num = 1

    while max_num < N:
        max_num += 6 * floor 
        floor += 1
    
    print(floor)

