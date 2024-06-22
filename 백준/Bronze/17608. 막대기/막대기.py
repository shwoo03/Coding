import sys
input = sys.stdin.readline

n = int(input())
list_num = []

for i in range(n):
    list_num.append(int(input()))

index = list_num.index(max(list_num))
list_num = list_num[index:]
max_num = list_num[-1]
result = 1
for i in range(len(list_num)-1,-1,-1):
    if max_num < list_num[i]:
        max_num = list_num[i]
        result += 1

print(result)