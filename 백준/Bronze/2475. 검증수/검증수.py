import math
import heapq
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline



if __name__ == "__main__":
    list_num = list(map(int, input().split(" ")))
    for i in range(len(list_num)):
        list_num[i] = list_num[i] ** 2

    print(sum(list_num) % 10)
