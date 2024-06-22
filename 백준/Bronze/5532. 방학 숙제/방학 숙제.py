l = int(input())
a = int(input())
b = int(input())
c = int(input()) 
d = int(input())

kor_rq_day = 0
while a > 0:
    a -= c
    kor_rq_day += 1

math_rq_day = 0
while b > 0:
    b -= d
    math_rq_day +=1

print(l - (max(kor_rq_day,math_rq_day)))