n = int(input())

list_num = [0,1]

for i in range(n-1):
    list_num.append(list_num[i]+list_num[i+1])

print(list_num[-1])