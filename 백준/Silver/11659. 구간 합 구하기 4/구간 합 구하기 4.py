import math
from collections import deque
import sys
input = sys.stdin.readline





if __name__ == "__main__":
    n,m = map(int,input().split())
    list_num = list(map(int,input().split()))
    S = [0] * n
    S[0] = list_num[0]

    for i in range(1, n):
        S[i] = S[i-1] + list_num[i]
    
    for _ in range(m):
        start, end = map(int, input().split())
        if start == 1:
            print(S[end - 1])
        else:
            print(S[end - 1] - S[start - 2])


