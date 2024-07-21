N = int(input())

list_num = []

for i in range(N):
    x, y = map(int, input().split())
    
    list_num.append((x, y))

list_num.sort()

for i in list_num:
    print(i[0], i[1])