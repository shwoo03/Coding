# 2차원 평면 위에 점 N 개 
# 1차 : y좌표 증가 순 / 2차 : x 좌표 증가 순 

N = int(input())
list_num = []

for i in range(N):
    temp_list = list(map(int, input().split()))
    list_num.append(temp_list)

list_num.sort(key=lambda p: (p[1], p[0]))

for x, y in list_num:
    print(x, y)