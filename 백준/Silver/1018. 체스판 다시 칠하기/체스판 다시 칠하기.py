# MN개의 단위 정사각형으로 나누어져 있는 M x N 크기의 보드를 찾음
# 검은색, 흰색으로 나누어져 칠해져 있다. 
# 이 보드를 잘라서 8 x 8 크기의 체스판으로 만들려고 한다.

# 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다.
# 각 칸이 검은색과 흰색 중 하나로 색칠되어 있다. 
# 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있다. 
# 따라서, 2가지 경우가 존재함 
# 1. 맨 왼쪽 위 칸이 흰색인 경우
# 2. 맨 왼쪽 위 칸이 검은색인 경우
# 8 x 8 크기의 체스판으로 잘라낸 뒤에 다시 칠하는 경우 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램 작성 

N, M = map(int, input().split())
board = [input() for _ in range(N)]

min_count = float('inf')  # 최소값을 찾기 위해 초기값을 무한대로 설정

for i in range(N - 7):
    for j in range(M - 7):
        count1 = 0 # 첫칸 W 일때 
        count2 = 0 # 첫칸 B 일때

        for k in range(8):
            for l in range(8):
                if (k + l) % 2 == 0:
                    if board[i + k][j + l] != 'W':
                        count1 += 1
                    if board[i + k][j + l] != 'B':
                        count2 += 1
                else:
                    if board[i + k][j + l] != 'B':
                        count1 += 1
                    if board[i + k][j + l] != 'W':
                        count2 += 1

        min_count = min(min_count, count1, count2)

print(min_count)
