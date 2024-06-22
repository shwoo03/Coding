for i in range(3):
    list_num = list(map(int,input().split()))
    if list_num.count(0) == 1:
        print("A")
    elif list_num.count(0) == 2:
        print("B")
    elif list_num.count(0) == 3:
        print("C")
    elif list_num.count(0) == 4:
        print("D")
    elif list_num.count(0) == 0:
        print("E")


