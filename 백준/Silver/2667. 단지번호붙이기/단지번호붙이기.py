import math
import heapq
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline


# 1은 집이 있는 곳을 0은 집이 없는 곳을 의미한다. 
# 각 단지에 속한 집의 수를 오름차순으로 정렬해서 출력해야 한다.

# 1. bfs 함수를 만들고 맨 마지막에 결과 값 보내주기 
# 2. 받고 정렬해서 출력 

def bfs(graph, N, visited, row, col):
    queue = deque()
    queue.append((row, col))
    visited[row][col] = True
    count = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1 and visited[nx][ny] == False:
                    count += 1
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    
    return count





if __name__ == "__main__":
    N = int(input())
    graph = []
    total_num = 0

    for i in range(N):
        graph.append(list(map(int, input().strip())))

    visited = [[False] * N for _ in range(N)]   
    list_result = []

    for row in range(N):
        for col in range(N):
            if visited[row][col] == False and graph[row][col] == 1:
                list_result.append(bfs(graph, N, visited, row, col))
                total_num += 1
    
    list_result.sort()
    print(total_num)
    for num in list_result:
        print(num)
