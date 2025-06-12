import math
import heapq
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline


# 

if __name__ == "__main__":
    ISBN = input().strip()

    for i in range(10):
        new_ISBN = ISBN.replace('*', str(i))
        sum = 0

        for j in range(12):
            if j % 2 == 0:
                sum += int(new_ISBN[j])
            else:
                sum += int(new_ISBN[j]) * 3

                m = int(new_ISBN[12])
        
        if (sum + m) % 10 == 0:
            print(i)
            break