T = int(input())

for i in range(T):
    list_num = list(map(int, input().split()))
    list_num = sorted(list_num)
    print(list_num[-3])

