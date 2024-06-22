total_price = int(input())
n = int(input())

check = 0
for i in range(n):
    price,num = map(int,input().split())
    check += price * num

if check == total_price:
    print("Yes")
else:
    print("No")