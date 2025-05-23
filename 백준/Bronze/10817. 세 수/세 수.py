import math
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline





if __name__ == "__main__":
    list_num = list(map(int, input().split()))
    list_num.sort()
    print(list_num[1])
    