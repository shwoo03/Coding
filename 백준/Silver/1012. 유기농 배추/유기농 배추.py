# 배추흰지렁지?가 한 마리라도 살고 있으면 다른 배추로 이동할 수 있어서 
# 그 배추들 또한 보호를 받을 수 있음 
# 한 마리의 지렁지가 인접 배추를 모두 보호할 수 있음
# 배추를 모두 보호하기 위해 필요한 최소 지렁지의 수를 구해야함

def dfs(x, y):
    # 그룹마다 한 마리의 지렁이가 필요함 상,하,좌,우 탐색하면서 전부 방문처리하면 됨 
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < row and 0 <= ny < col:
            if cabbage_map[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)




if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)  

    T = int(input())

    for _ in range(T):
        col, row, cabbage = map(int, input().split())
        cabbage_map = [[0] * col for _ in range(row)]
        visited = [[0] * col for _ in range(row)]

        for _ in range(cabbage):
            y, x = map(int, input().split())
            cabbage_map[x][y] = 1

        worm_num = 0
        for i in range(row):
            for j in range(col):
                if cabbage_map[i][j] == 1 and not visited[i][j]:
                    # dfs 함수가 방문처리 해주고 다시 for를 돌면서
                    # 방문처리 안된 배추를 만나면 새로운 그룹이므로 +1 
                    dfs(i, j)
                    worm_num += 1
        
        print(worm_num)
