import math
import heapq
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline


# 최소 힙 사용해서 삽입, 삭제 구현 


if __name__ == "__main__":
    heap = []
    n = int(input())

    for i in range(n):
        num = int(input())

        if num != 0:
            heapq.heappush(heap, num)
        else:
            if heap:
                print(heapq.heappop(heap))
            else:
                print(0)