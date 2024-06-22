while(True):
    list_num = list(map(int,input().split()))
    if sum(list_num) == 0:
        exit()
    list_num.sort()
    if max(list_num)**2 == list_num[0]**2 + list_num[1]**2:
        print("right")
    else:
        print("wrong")