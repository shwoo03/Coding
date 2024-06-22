list_time = []

for i in range(4):
    t = int(input())
    list_time.append(t)

total_t = sum(list_time)

second = total_t
minute = 0

while second >= 60:
    second -= 60
    minute += 1

print(minute)
print(second)