sum = 0
min = 101
for i in range(7):
    n = int(input())
    if n % 2 != 0:
        sum += n
        if min > n:
            min = n


if min == 101:
    print(-1)
else:
    print(sum)
    print(min)