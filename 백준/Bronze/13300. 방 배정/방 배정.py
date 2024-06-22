import math

n,k = map(int,input().split())
# 1~6 학년 까지의 남녀 리스트 생성 
student = [[0] * 2 for _ in range(6)]

for i in range(n):
    s,grade = map(int,input().split())
    student[grade-1][s-1] += 1

result = 0
for i in range(6):
    for j in range(2):
        result = result + math.ceil(student[i][j] / k)

print(result)




