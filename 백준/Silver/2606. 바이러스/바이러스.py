import math
from collections import deque
import sys
input = sys.stdin.readline


# bfs 통해서 1과 연결된 모든 인접 노드를 알면 됨 
def bfs(matrix, num_computer, start=0):
    visited = [False] * num_computer
    visited[start] = True
    queue = deque([start])
    result = 0

    while queue:
        node = queue.popleft()

        for neighbor in range(num_computer):
            if matrix[node][neighbor] == 1 and not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                result += 1
    
    return result 


if __name__ == "__main__":
    num_computer = int(input())
    num_connection = int(input())
    matrix = [[0 for i in range(num_computer)] for j in range(num_computer)]

    for i in range(num_connection):
        x,y = map(int,input().split())
        matrix[x-1][y-1] = 1
        matrix[y-1][x-1] = 1
    
    print(bfs(matrix, num_computer))
