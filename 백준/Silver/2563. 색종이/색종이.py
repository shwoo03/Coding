# 가로, 세로 크기를 100인 정사각형 모양의 흰색 도화지가 존재한다.
# 정사각형 모양의 10 X 10 크기의 색종이를 도화지의 변이 평행하도록 붙인다.
# 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오. 

N = int(input())

result = 0
paper = [[0] * 100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())
    
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

result = 0
for row in paper:
    result += row.count(1)


print(result)