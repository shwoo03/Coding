import math
import heapq
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    for line in sys.stdin:
        a, b = map(int, line.split())
        print(a + b)