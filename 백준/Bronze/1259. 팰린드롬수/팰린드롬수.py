import math
import heapq
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline


# 팰린드롬 인지 확인하는 코드 작성 



if __name__ == "__main__":
    while True:
        word = input().strip()

        if word == '0':
            break

        if word == word[::-1]:
            print("yes")
        else:
            print("no")