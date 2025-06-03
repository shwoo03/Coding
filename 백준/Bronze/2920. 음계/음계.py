import math
import heapq
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline



if __name__ == "__main__":
    list_num = list(map(int, input().split()))

    if list_num == sorted(list_num):
        print("ascending")
    elif list_num == sorted(list_num, reverse=True):
        print("descending")
    else:
        print("mixed")
