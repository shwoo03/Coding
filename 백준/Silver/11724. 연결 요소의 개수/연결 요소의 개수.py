import math
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


# 무방향 그래프에서 연결 요소 구하는 프로그램 작성 
# 탐색을 통해서 연결 요소의 집합을 찾으면 된다.
def BFS(start, visited, graph):
    visited[start] = True
    queue = deque([start])

    while queue:
        node = queue.popleft()

        for neighbor in range(len(graph[node])):
            if not visited[neighbor] and graph[node][neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True



if __name__ == "__main__":
    node, edge = map(int,input().split())
    graph = [[0 for i in range(node)] for i in range(node)]
    
    for i in range(edge):
        x, y = map(int,input().split())
        x = x - 1
        y = y - 1
        graph[x][y] = 1
        graph[y][x] = 1
    
    count = 0
    visited = [False] * node

    for i in range(node):
        if not visited[i]:
            BFS(i, visited, graph)
            count += 1
    
    print(count)
