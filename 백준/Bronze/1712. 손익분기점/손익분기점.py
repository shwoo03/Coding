# 매년 A의고정 비용 
# 한 대당 B의 가변 비용 
# 노트북 가격은 C
# 총 수입(판매 비용) - 총 비용(고정비용+가변비용) > 0 이 손익 분기점이다. 

a,b,c = map(int,input().split())
x = 1  # x 는 판매수량 

if b >= c:
    print(-1)
else:
    x = a // (c - b) + 1
    print(x)
