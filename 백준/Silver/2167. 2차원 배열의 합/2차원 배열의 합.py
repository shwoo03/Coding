# 2 차원 배열이 주어졌을 때 i,j 위치부터 x,y 위치까지의 합을 구하는 프로그램 작성 
# i,j 는 각각 행, 열을 나타냄 

N,M = map(int, input().split())

list_num = []
for _ in range(N):
    row = list(map(int, input().split()))
    list_num.append(row)

prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        prefix_sum[i][j] = list_num[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]


K = int(input())
for i in range(K):
    i,j,x,y = map(int, input().split())
    total_sum = prefix_sum[x][y] - prefix_sum[i-1][y] - prefix_sum[x][j-1] + prefix_sum[i-1][j-1]
    
    print(total_sum)