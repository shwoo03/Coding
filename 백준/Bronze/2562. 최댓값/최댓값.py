list_num = []
for i in range(9):
    list_num.append(int(input()))

print(max(list_num))
print(list_num.index(max(list_num))+1)