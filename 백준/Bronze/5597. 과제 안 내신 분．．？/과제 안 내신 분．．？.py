list_num = [i for i in range(1,31)]

for i in range(28):
    a = int(input())
    list_num.remove(a)

sorted(list_num)
for i in list_num:
    print(i)