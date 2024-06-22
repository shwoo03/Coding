n , m = map(int,input().split())
list_num = [0 for i in range(n)]

for i in range(m):
    i, j, k = map(int,input().split())
    for index in range(i-1,j,1):
        list_num[index] = k

print(*list_num)
