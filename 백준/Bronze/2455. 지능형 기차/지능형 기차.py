n = 0
max = 0

for i in range(4):
    ex,ride = map(int,input().split())
    n += ride
    n -= ex
    if max < n:
        max = n

print(max)