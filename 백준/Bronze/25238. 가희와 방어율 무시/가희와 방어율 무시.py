a,b = map(int,input().split())

result = a - (a * (b/100))
if result >= 100:
    print(0)
else:
    print(1)