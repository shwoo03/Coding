import math
import heapq
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    while True:
        a, b = map(int,input().split())
        if a == 0 and b == 0:
            break
        else:
            print(a+b)