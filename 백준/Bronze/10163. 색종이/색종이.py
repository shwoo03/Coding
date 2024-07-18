# 색깔이 다른 직사각형 모양의 색종이가 수직 아니면 평면으로 놓인다.
# N장의 색종이가 주어진 위치에 차례로 놓일 때, 각 색종이가 놓인 부분의 넓이를 구하시오.

# 색종이 장수 N
N = int(input())

#색종이의 넓이를 저장할 리스트 
# 101 x 101 크기의 0으로 초기화된 2차원 리스트 생성
paper = [[0 for _ in range(101)] for _ in range(101)]

for paper_num in range(1, N + 1):
    x, y, width, height = map(int, input().split())


    for j in range(x, x + width):
        for k in range(y, y + height):
            paper[j][k] = paper_num


# 각 색종이의 넓이를 저장할 리스트
areas = [0] * N

# 각 색종이의 넓이를 계산
for j in range(101):
    for k in range(101):
        if paper[j][k] > 0:
            areas[paper[j][k] - 1] += 1

# 결과 출력
for area in areas:
    print(area)
