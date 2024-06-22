n,m = map(int,input().split())
list_num = [i for i in range(1,n+1)]

for i in range(m):
    a,b = map(int,input().split())
    if a == b:
        continue
    list_num[a-1],list_num[b-1] = list_num[b-1],list_num[a-1]

print(*list_num)