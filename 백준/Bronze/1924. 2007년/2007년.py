month,day = map(int,input().split())
total_day = day

for i in range(1,month):
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
        total_day += 31
    elif i == 2:
        total_day += 28
    else:
        total_day += 30

total_day %= 7
if total_day == 1:
    print("MON")
elif total_day == 2:
    print("TUE")
elif total_day == 3:
    print("WED")
elif total_day == 4:
    print("THU")
elif total_day == 5:
    print("FRI")
elif total_day == 6:
    print("SAT")
else:
    print("SUN")