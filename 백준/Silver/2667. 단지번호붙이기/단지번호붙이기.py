import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# 정사각형 배열에서 0,1로 나누어 지는데
# 각 1의 그룹의 개수를 확인해야 한다.

# 상하좌우를 탐색하면서 1의 그룹을 찾고 
# bfs로 탐색 
from collections import deque

def bfs_find_houses(houses, visited, result_list):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    house_count = 0

    for i in range(len(houses)):
        for j in range(len(houses)):
            if houses[i][j] == 1 and not visited[i][j]:
                # 첫 그룹 시작점 찾고 1로 초기화
                queue.append((i,j))
                visited[i][j] = True
                house_count = 1

                while queue:
                    x, y = queue.popleft()
                    
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < len(houses) and 0 <= ny < len(houses) and not visited[nx][ny] and houses[nx][ny] == 1:
                            queue.append((nx, ny))
                            visited[nx][ny] = True
                            house_count += 1
                result_list.append(house_count)





if __name__ == "__main__":
    N = int(input())
    houses = [list(map(int, input().rstrip())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    result_list = []

    bfs_find_houses(houses, visited, result_list)
    result_list.sort()

    print(len(result_list))
    for result in result_list:
        print(result)