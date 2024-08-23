# N 장의 카드가 있다.
# 각각의 카드는 차례로 1부터 N까지의 번호가 있음 
# 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.
# 이제 제일 위에 있는 카드를 바닥에 버린다.
# 그 다음 제일 위에 있는 카드를 제일 아래에 잇는 카드 밑으로  옮긴다.

N = int(input())
list_num = list(range(1, N + 1))  

index = 0 
while len(list_num) - index > 1: 
    index += 1  
    list_num.append(list_num[index]) 
    index += 1  

print(list_num[index])  