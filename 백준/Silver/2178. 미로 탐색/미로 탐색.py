import math
import heapq
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline


# 미로 받아서 N, M에 도달할 수 있는 최소 거리를 구하는 문제 

def bfs(graph, N, M):
    queue = deque()
    queue.append((0,0))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
    
    return graph[N - 1][M - 1]




if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = []
    for i in range(N):
        graph.append(list(map(int ,input().strip())))
    
    print(bfs(graph, N, M))