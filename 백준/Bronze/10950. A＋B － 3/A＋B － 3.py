import math
import heapq
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    T = int(input())

    for i in range(T):
        a, b = map(int,input().split())
        print(a+b)