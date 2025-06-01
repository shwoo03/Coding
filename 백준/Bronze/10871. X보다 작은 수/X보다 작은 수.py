import math
import heapq
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline




# x보다 작은 수
if __name__ == "__main__":
    N, X = map(int,input().split())
    list_num = list(map(int, input().split()))

    for num in list_num:
        if num < X:
            print(num, end=" ")