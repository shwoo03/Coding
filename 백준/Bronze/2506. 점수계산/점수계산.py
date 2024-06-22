n = int(input())
result = 0
plus = 1
list_score = list(map(int,input().split()))

for i in range(n):
    if list_score[i] == 1:
        result += plus
        plus += 1
    elif list_score[i] == 0:
        plus = 1

print(result)