import math
import heapq
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline


# N 명의 참가자가 존재할 때 사이즈별 티셔츠를 나눠줘야 한다.
#   티셔츠는 주문할 때 T장 씩 구매가능 / 펜은 P자루 또는 한개 식 주문 가능 
# 티셔츠와 펜을 최소 몇 묶음씩 구매해야 하는지 구하는 프로그램
#   티셔츠는 -> sum(각 사이즈 별 티셔츠 수의 묶음 )
#   펜 ->  N // P + N % P

if __name__ == "__main__":
    N = int(input())
    list_num = list(map(int,input().split()))
    list_T_result = []
    T, P = map(int,input().split())

    for shirts in list_num:
        if shirts % T == 0:
            list_T_result.append(shirts // T)
        else:
            list_T_result.append((shirts // T) + 1)
    
    set_pen = N // P
    pen = N % P
    print(sum(list_T_result))
    print(f"{set_pen} {pen}")
