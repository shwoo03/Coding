a,b = map(int,input().split())
price = int(input())

if a + b < price*2:
    print(a+b)
else:
    print(a+b-price*2)