# 어떤 방은 N X N 크기의 정사각형 모양이다.
# 여기서 누울 자리를 찾아야 하는데, 2칸 이상의 빈 칸이 존재하면 누울 수 있다.
# 가로로, 세로로 누울 수 있고, 누울 때는 무조건 벽이나 짐에 닿게 된다.

# . 은 빈 칸, X는 짐이다. 

N = int(input())
room = []

for i in range(N):
    room.append(list(input()))

count_width = 0  # 가로
count_length = 0  # 세로

# 가로 체크하는 for 문 
for i in range(N):
    count = 0 
    for j in range(N):
        if room[i][j] == '.':
            count += 1
        else:
            if count >= 2:
                count_width += 1
            count = 0
    if count >= 2:  # 마지막 열 체크
        count_width += 1

# 세로 체크하는 for 문 
for i in range(N):
    count = 0
    for j in range(N):
        if room[j][i] == '.':
            count += 1
        else:
            if count >= 2:
                count_length += 1
            count = 0
    if count >= 2:  # 마지막 행 체크
        count_length += 1

print(count_width, count_length)