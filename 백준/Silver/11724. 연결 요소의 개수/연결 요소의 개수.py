import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline



# 무방향 그래프에서 연결 요소의 개수를 구하는 프로그램 작성 
# dfs 써서 gourp 이 몇개인지 확인하면 됨 

def dfs(v, matrix, visited, group_count):
    visited[v] = 1

    for i in range(1, len(matrix)):
        if matrix[v][i] == 1 and visited[i] == 0:
            dfs(i, matrix, visited, group_count)




if __name__ == "__main__":
    # 인접 행렬 
    N, M = map(int, input().split())

    matrix = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        a,b = map(int, input().split())
        matrix[a][b] = 1
        matrix[b][a] = 1
    

    visited = [0] * (N + 1)
    group_count = 0

    for i in range(1, N + 1):
        if visited[i] == 0:
            dfs(i, matrix, visited, group_count)
            group_count += 1
    
    print(group_count)



