import math
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


# 스택을 사용해서 1부터 n까지 증가하고 받은 수열이 완성되는지 확인


if __name__ == "__main__":
    result = []
    stack = []
    T = int(input())
    input_list = []

    for i in range(T):
        input_list.append(int(input()))
    
    for i in range(1, T+1):
        stack.append(i)
        result.append('+')

        while True:
            if stack:
                if stack[-1] == input_list[0]:
                    result.append("-")
                    stack.pop()
                    input_list.pop(0)
                else:
                    break
            else:
                break

    
    if stack:
        print("NO")
    else:
        for ch in result:
            print(ch)


