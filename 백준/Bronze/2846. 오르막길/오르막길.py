N = int(input())
list_num = list(map(int, input().split()))

index = 0
measurment = 0

while index < N - 1:
    low_h = list_num[index]
    
    while index < N - 1 and list_num[index] < list_num[index + 1]:
        index += 1
    

    high_h = list_num[index]


    if high_h - low_h > measurment:
        measurment = high_h - low_h
    
    while index < N - 1 and list_num[index] >= list_num[index + 1]:
        index += 1

print(measurment)
