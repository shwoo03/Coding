day = int(input())

list_num = list(map(int,input().split()))

result = 0
for i in list_num:
    if day == i:
        result += 1

print(result)