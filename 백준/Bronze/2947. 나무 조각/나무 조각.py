list_num = list(input().split())

index = 0
while True:
    if list_num[index] > list_num[index + 1]:
        list_num[index], list_num[index + 1] = list_num[index + 1], list_num[index]
        print(*list_num)
        
    
    index += 1
    
    if list_num == sorted(list_num):
        break
    elif index == len(list_num) - 1:
        index = 0