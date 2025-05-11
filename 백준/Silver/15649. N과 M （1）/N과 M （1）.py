import math
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline


# N, M이 주어지면 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열을 모두 구하는 프로그램
if __name__ == "__main__":
    row, col = map(int,input().split())
    nums = list(range(1, row+1))

    for i in permutations(nums, col):
        print(*i)





