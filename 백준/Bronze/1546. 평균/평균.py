n = int(input())
list_score = list(map(int,input().split()))
m = max(list_score)

for i in range(n):
    list_score[i] = list_score[i] / m * 100

print(sum(list_score)/n)