n = int(input())
money = 1000 - n

m500 = money // 500
money %= 500
m100 = money // 100
money %= 100
m50 = money // 50
money %= 50
m10 = money // 10
money %= 10
m5 = money // 5
money %= 5
m1 = money // 1

print(m500+m100+m50+m10+m5+m1)