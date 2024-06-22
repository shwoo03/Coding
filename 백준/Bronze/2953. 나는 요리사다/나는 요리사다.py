max = 0
index = 0
for i in range(1,6,1):
    list_num = list(map(int,input().split()))
    if max < sum(list_num):
        max = sum(list_num)
        index = i

print(f"{index} {max}")
