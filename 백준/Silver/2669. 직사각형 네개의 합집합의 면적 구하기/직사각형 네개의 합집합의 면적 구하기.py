# 네 개의 직사각형이 있는데 밑면은 모두 가로축에 평행하다.
# 이 네 개의 직사각형들이 차지하는 면적을 구하는 프로그램을 작성하시오.

# 1,2 정수는 직사각형의 왼쪽 아래 꼭짓점의 x좌표, y좌표이고
# 3,4 정수는 직사각형의 오른쪽 위 꼭짓점의 x좌표, y좌표이다.

list_coordinate = []
grid = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(4):
    list_coordinate.append(list(map(int, input().split())))

for i in range(4):
    for j in range(list_coordinate[i][0], list_coordinate[i][2]):
        for k in range(list_coordinate[i][1], list_coordinate[i][3]):
            grid[j][k] = 1

result = 0
for i in range(100):
    result += sum(grid[i])

print(result)