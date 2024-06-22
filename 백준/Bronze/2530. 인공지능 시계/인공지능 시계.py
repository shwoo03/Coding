hour,minute,second = map(int,input().split())
rq_second = int(input())

hour = hour + (rq_second // 3600)
rq_second = rq_second % 3600

minute = minute + (rq_second // 60)
rq_second = rq_second % 60

second += rq_second

while second >= 60:
    second -= 60
    minute += 1

while minute >= 60:
    minute -= 60
    hour += 1

while hour >= 24:
    hour -= 24

print(hour, minute, second)