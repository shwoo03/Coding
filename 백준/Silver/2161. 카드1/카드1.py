# N 장의 카드가 있다. 차례로 1부터 N까지의 번호가 붙어 있다.
# 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.

# 이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다.
# 우선, 제일 위에 있는 카드를 바닥에 버린다.
# 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
# N이 주어졌을 때, 버린 카드들을 순서대로 출력하고, 마지막에 남게 되는 카드를 출력하는 프로그램을 작성하시오.

N = int(input())
cards = [i for i in range(1, N+1)]

result = []
while len(cards) > 1: 
    result.append(cards.pop(0))
    cards.append(cards.pop(0))

for i in result:
    print(i, end=' ')
print(cards[0])