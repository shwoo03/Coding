list_num = list(map(int,input().split()))

if list_num == sorted(list_num):
    print("ascending")
elif list_num == sorted(list_num, reverse=True):
    print("descending")
else:
    print("mixed")