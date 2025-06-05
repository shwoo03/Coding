import math
import heapq
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    while True:
        list_num = list(map(int,input().split()))
        list_num.sort()

        if list_num == [0, 0, 0]:
            break

        if list_num[2] ** 2 == (list_num[0] ** 2 + list_num[1] ** 2):
            print("right")
        else:
            print("wrong")