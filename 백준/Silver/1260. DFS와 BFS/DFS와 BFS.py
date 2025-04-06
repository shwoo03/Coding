# DFS, BFS로 탐색한 결과를 출력하는 프로그램 
# 1. 방문 가능한 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문한다.
# 2. 더 이상 방문할 수 없는 점이 없는 경우 종료.
# 3. 정점 번호는 1 ~ N 까지 


# DFS
def dfs(graph, start, visited):
    visited[start] = 1
    print(start, end=' ')

    for i in range(1, len(graph)):
        if graph[start][i] == 1 and visited[i] == 0:
            dfs(graph, i, visited)



def bfs(graph, start, visited):
    queue = [start]
    visited[start] = 1
    print(start, end=' ')

    while queue:
        v = queue.pop(0)
        for i in range(1, len(graph)):
            if graph[v][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                print(i, end=' ')




if __name__ == '__main__':
    N, M, V = map(int, input().split())
    
    # 인접 행렬로 접근 
    graph = [[0] * (N + 1) for _ in range(N + 1)]

    # 정보 입력 
    for _ in range(M):
        a,b = map(int, input().split())
        graph[a][b] = 1
        graph[b][a] = 1
    
    # 방문 여부 
    visited = [0] * (N + 1)

    dfs(graph, V, visited)
    print()


    visited = [0] * (N + 1)
    bfs(graph, V, visited)




