N = int(input())

# 4,3,2,1 순으로 별, 동그라미, 네모, 세모 
for i in range(N):
    str = list(input().split())
    num_a = int(str[0])
    list_A = list(map(int, str[1:]))
    
    str = list(input().split())
    num_b = int(str[0])
    list_B = list(map(int, str[1:]))
    
    if list_A.count(4) > list_B.count(4):
        print('A')
    elif list_A.count(4) < list_B.count(4):
        print('B')
    elif list_A.count(3) > list_B.count(3):
        print('A')
    elif list_A.count(3) < list_B.count(3):
        print('B')
    elif list_A.count(2) > list_B.count(2):
        print('A')
    elif list_A.count(2) < list_B.count(2):
        print('B')
    elif list_A.count(1) > list_B.count(1):
        print('A')
    elif list_A.count(1) < list_B.count(1):
        print('B')
    else:
        print('D')