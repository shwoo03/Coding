N = int(input())
list_num = list(map(int, input().split()))

M = int(input())
dict_num = {
    
}

list_input = list(map(int, input().split()))

for i in list_input:
    dict_num[i] = 0

for i in list_num:
    if i in dict_num:
        dict_num[i] += 1

for i in list_input:
    print(dict_num[i], end=' ')