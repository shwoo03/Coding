import math
import heapq
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    a = input().strip()
    b = input().strip()
    c = input()

    ab = a + b
    print(int(a) + int(b) - int(c))
    print(int(ab) - int(c))