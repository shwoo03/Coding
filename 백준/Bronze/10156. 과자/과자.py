danga,num,money = map(int,input().split())

rq_money = danga * num - money

if rq_money < 0:
    print(0)
else:
    print(rq_money)