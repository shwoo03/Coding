import math
import heapq
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline



if __name__ == "__main__":
    y = int(input())

    if((y % 4 == 0) and (y % 100 != 0)) or (y % 400 == 0):
        print(1)
    else:
        print(0)