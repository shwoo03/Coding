# 1 = 1           n = 0
# 2~7 = 2         n = 1
# 8~19 = 3        n = 2
# 20~37 = 4       n = 3
# 38~61 = 5       n = 4

#즉, 처음 6 증가하고 증가값은 6씩 증가된다. 
# 그렇다면 while 입력값 > 최대 방 번호 를 해서 루프를 돌리면 된다 .

room_num = int(input())

p_num = 1 #벌집 개수 1부터 시작 
cnt = 1
while room_num > p_num:
    p_num += 6 * cnt
    cnt += 1

print(cnt)
        