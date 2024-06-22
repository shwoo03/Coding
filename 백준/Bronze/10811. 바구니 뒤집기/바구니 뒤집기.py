n,m = map(int,input().split())
list_num = [i for i in range(1,n+1)]

for i in range(m):
    a,b = map(int,input().split())
    a_index = a - 1
    b_index = b - 1
    if a_index == b_index:
        continue
    else:
        while True:
            list_num[a_index],list_num[b_index] = list_num[b_index],list_num[a_index]
            a_index += 1
            b_index -= 1
            if a_index >= b_index:
                break

print(*list_num)