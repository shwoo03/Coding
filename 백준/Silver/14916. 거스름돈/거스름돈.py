# 춘향이는 편의점에서 일한다.
# 손님이 2원짜리와 5원짜리로 거스름돈을 달라고 한다. 
# 동전의 개수가 최소가 되도록 거슬러 주어야 한다.
# 거수름돈이 n 일 경우, 최소 동전의 개수를 구하시오.
# 만약 거슬러 줄 수 없으면 -1을 출력한다. 

n = int(input())
won5 = 0
won2 = 0

while True:
    if n < 0:
        print(-1)
        break
    
    if n % 5 == 0:
        won5 = n // 5
        print(won5 + won2)
        break
    
    n -= 2
    won2 += 1
