n = int(input())
list_num = []

for i in range(n):
    list_num.append(int(input()))

list_num.sort()
for i in list_num:
    print(i)