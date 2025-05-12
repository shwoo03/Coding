import math
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline


# DFS, BFS 탐색 결과를 출력하는 프로그램 작성 
# 방문할 수 있는 정점이 여러 개면 정점 번호가 작은 것 먼저 방문 

def DFS(v, graph, visited, N):
    visited[v] = True
    print(v, end=' ')
    
    for i in range(1, N + 1):
        if graph[v][i] == 1 and not visited[i]:
            DFS(i, graph, visited, N)



def BFS(v, graph, visited, N):
    queue = deque([v])
    visited[v] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for i in range(1, N + 1):
            if graph[node][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)





if __name__ == "__main__":
    N, M, V = map(int,input().split())
    graph = [[0 for i in range(N+1)] for j in range(N+1)]
    
    for i in range(M):
        x, y = map(int,input().split())
        graph[x][y] = 1
        graph[y][x] = 1
    

    visited_dfs = [False] * (N + 1)
    DFS(V, graph, visited_dfs, N)
    print()

    visited_bfs = [False] * (N + 1)
    BFS(V, graph, visited_bfs, N)
    print()