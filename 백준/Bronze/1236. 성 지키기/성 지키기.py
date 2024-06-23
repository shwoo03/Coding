# 모든 행과 열에 한 명 이상의 경비원 존재 
# 성의 크기와 경비원이 어디 있는지 주면, 몇명이 더 필요한지 출력

# 입력 N,M == 성의 가로, 세로 크기 

N, M = map(int, input().split())
list_castle = []

# 성의 상태 입력
for i in range(N):
    list_castle.append(input())

row_guard = 0
col_guard = 0

for i in range(N):
    if 'X' not in list_castle[i]:
        row_guard += 1

for i in range(M):
    is_guard = False
    for j in range(N):
        if list_castle[j][i] == 'X':
            is_guard = True
            break
    if not is_guard:
        col_guard += 1

print(max(row_guard, col_guard))