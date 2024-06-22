for i in range(3):
    list_time = list(map(int,input().split()))
    hour = list_time[3] - list_time[0]
    minute = list_time[4] - list_time[1]
    second = list_time[5] - list_time[2]

    if second < 0:
        second += 60
        minute -= 1

    if minute < 0:
        minute += 60
        hour -= 1
    
    print(hour, minute, second)