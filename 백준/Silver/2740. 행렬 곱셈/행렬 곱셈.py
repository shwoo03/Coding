#N*M 크기의 행렬 A와 M*K 크기의 행렬 B가 주어졌을 때, 두 행렬을 곱하는 프로그램을 작성하시오.

N, M = map(int, input().split())

list_A = []
for i in range(N):
    list_A.append(list(map(int, input().split())))

list_B = []
M, K = map(int, input().split())
for i in range(M):
    list_B.append(list(map(int, input().split())))

# 행렬 A와 B의 곱셈 결과를 저장할 행렬 C 생성
list_C = [[0] * K for _ in range(N)]

# 행렬 곱셈 수행
for i in range(N):
    for j in range(K):
        for k in range(M):
            list_C[i][j] += list_A[i][k] * list_B[k][j]

# 행렬 C 출력
for row in list_C:
    print(*row)