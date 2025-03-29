# 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하라.
# 컴퓨터의 수가 주어지고 
# 각 컴퓨터가 연결된 정보가 주어짐.

computers = int(input())
connections = int(input())

# 행렬 생성 (인접 행렬 생성, 무방향 그래프)
graph = [[0] * (computers + 1) for _ in range(computers + 1)]


for i in range(connections):
    a, b = map(int, input().split())
    # 연결된 컴퓨터는 1로 표시
    graph[a][b] = 1
    graph[b][a] = 1


# 감염 컴퓨터
infected = [0] * (computers + 1)
infected[1] = 1 
infected_count = 0 # 감염된 컴퓨터 수


# visited 리스트 
visited = [0] * (computers + 1) 
visited[1] = 1 


# DFS 
stack = [1] 
while stack:
    current = stack.pop()
    for i in range(1, computers + 1):
        if graph[current][i] == 1 and visited[i] == 0:
            stack.append(i)
            visited[i] = 1
            infected[i] = 1
            infected_count += 1

# 감염된 컴퓨터 수 출력
print(infected_count)