list_num = []

for i in range(9):
    list_num.append(list(map(int,input().split())))

row_index = 0
col_index = 0
max = 0
for i in range(9):
    for r in range(9):
        if max < list_num[i][r]:
            max = list_num[i][r]
            row_index = i
            col_index = r

print(max)
print(row_index+1, col_index+1)