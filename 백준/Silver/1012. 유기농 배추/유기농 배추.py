import math
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


# 배추가 주어지면 배추가 이어진 그룹의 수를 알면 된다. 
# DFS로 탐색을 진행하고 인접한 모든 그룹을 True로 바꾸면 됨 
def DFS(graph, visited, row, col):
    visited[row][col] = True
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        nx = col + dx[i]
        ny = row + dy[i]

        if 0 <= nx < len(graph[0]) and 0 <= ny < len(graph):
            if graph[ny][nx] == 1 and (visited[ny][nx] != True):
                DFS(graph, visited, ny, nx)




if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        width, length, K = map(int,input().split())
        graph = [[0 for _ in range(width)] for _ in range(length)]
        visited = [[False for _ in range(width)] for _ in range(length)]

        for __ in range(K):
            col, row = map(int,input().split())
            graph[row][col] = 1
        
        count = 0
        for row in range(length):
            for col in range(width):
                if (visited[row][col] != True) and (graph[row][col] == 1):
                    DFS(graph, visited, row, col)
                    count += 1

        print(count)


