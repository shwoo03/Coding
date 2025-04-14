import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# N X M 크기의 배열로 표현되는 미로가 존재함 
# 1은 이동가능, 0은 이동 못함 
# (1,1) 에서 (N,M) 까지 가는 최단거리 구하기 


# 상하좌우 탐색을 통해서 이동 가능 여부를 확인함 
# BFS 알고리즘을 통해서 최단거리 구하기
def bfs(x, y, maze, visited):
    queue = [(x,y)]
    visited[x][y] = True
    distance = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        distance += 1
        
        for _ in range(len(queue)):
            x, y = queue.pop(0)
            if (x == len(maze) - 1) and (y == len(maze[0]) - 1):
                print(distance)
                return

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and not visited[nx][ny] and maze[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    
    print(-1)  





if __name__ == "__main__":
    x, y = map(int, input().split())
    maze = [list(map(int, input().rstrip())) for _ in range(x)]
    visited = [[False] * y for _ in range(x)]

    bfs(0, 0, maze, visited)
    


