# 김형택은 탑문고의 직원이다. 김형택은 계산대에서 계산을 하는 직원이다. 
# 김형택은 그날 근무가 끝난 후에, 오늘 판매한 책의 제목을 보면서 가장 많이 팔린 책의 제목을 칠판에 써놓는 일도 같이 하고 있다.
# 오늘 하루 동안 팔린 책의 제목이 입력으로 들어왔을 때, 가장 많이 팔린 책의 제목을 출력하는 프로그램을 작성하시오.

N = int(input())

book = {}

for _ in range(N):
    title = input()
    if title in book:
        book[title] += 1
    else:
        book[title] = 1

maxValue = max(sorted(book.keys()), key=lambda x: book[x])
print(maxValue)