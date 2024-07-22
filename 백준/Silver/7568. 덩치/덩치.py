# 덩치를 키, 몸무게 두 개의 값으로 등수를 매기려고 한다.
# a ( x, y ) b ( p, q ) 일 때, x > p, y > q 이면 a가 b보다 덩치가 크다.
# 하지만 둘 중 한개가 크고 한 개는 작으면 덩치를 비교할 수 없다.
# 이런 규칙으로 덩치를 비교했을 때 각 사람의 덩치 등수를 출력하라. 덩치를 비교할 수 없으면 공동 순위에 기록한다.

N = int(input())

list_info = []

for i in range(N):
    x, y = map(int, input().split())
    list_info.append((x, y))

for i in list_info:
    rank = 1
    for j in list_info:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    
    print(rank, end=' ')