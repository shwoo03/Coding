ls = [0] * 9

for i in range(9):
    ls[i] = int(input())
sum_ls = sum(ls)

for i in range(8):
    for j in range(i+1,9):
        if sum_ls - (ls[i] + ls[j]) == 100:
            x = ls[i]
            y = ls[j]
            break

ls.remove(x)
ls.remove(y)
ls.sort()
for i in ls:
    print(i)