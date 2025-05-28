import math
import heapq
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline


# 정수 삼각형이 존재할 때 좌/우 대각선을 골라서 내려왔을 때 그 합이 최대가 되도록 하는 프로그램 작성 
#   처음 든 생각은 어짜피 모든 경우의 수를 구해야하지 않을까였음 
#   100까지의 수만 나오다가 중간에 9999가 나오면 말짱 도루묵이니까 
#   그렇다면 어떻게 효과적으로 모든 경우의 수를 구할까 
#   max 함수를 사용해서 모든 열의 누적 합을 계속 위로 올리다보면 가장 위의 수가 최대값이 될 것이다.
#   결국 bottom-up 방식을 사용하면 됨 


if __name__ == "__main__":
    N = int(input())

    triangle = [list(map(int, input().split())) for _ in range(N)]
    
    for row in range(N-2, -1, -1):
        for col in range(len(triangle[row])):
            triangle[row][col] += max(triangle[row+1][col], triangle[row+1][col+1])
    
    print(triangle[0][0])



