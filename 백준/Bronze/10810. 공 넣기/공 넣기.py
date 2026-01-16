basket , n = map(int,input().split())
ball = [0 for i in range(basket)]

for i in range(n):
    x, y, number = map(int,input().split())
    
    for i in range(x-1, y):
        ball[i] = number

print(*ball)