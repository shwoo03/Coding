list_num = []

for i in range(5):
    a = int(input())
    list_num.append(a)

list_num.sort()
print(sum(list_num) // 5)
print(list_num[2])
