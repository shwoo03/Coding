N, M = map(int,input().split())

list_pocketmon = []
list_question = []

for i in range(N):
    list_pocketmon.append(input())

for i in range(M):
    list_question.append(input())

for i in list_question:
    if i.isdigit():
        print(list_pocketmon[int(i)-1])
    else:
        print(list_pocketmon.index(i)+1)