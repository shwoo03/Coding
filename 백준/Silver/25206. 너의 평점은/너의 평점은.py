# 졸업은 전공평점, 3.3 이상이거나 졸업고사 통과 
# 하지만, 치훈이는 졸업고사 응시 안함 
# 전공평점 3.3 이상인지 확인
# 전공 과목별 ( 학점 X 과목평점 ) 의 함을 학점의 총합으로 나눈 값 
# 이때 p/f는 학점에 포함되지 않음

import sys
input = sys.stdin.readline

credit = 0
total = 0

for _ in range(20):
    line = input().split()
    
    if line[2] == 'P':
        continue
    elif line[2] == 'F':
        total += 0
        credit += float(line[1])
    elif line[2] == 'A+':
        total += 4.5 * float(line[1])
        credit += float(line[1])
    elif line[2] == 'A0':
        total += 4.0 * float(line[1])
        credit += float(line[1])
    elif line[2] == 'B+':
        total += 3.5 * float(line[1])
        credit += float(line[1])
    elif line[2] == 'B0':
        total += 3.0 * float(line[1])
        credit += float(line[1])
    elif line[2] == 'C+':
        total += 2.5 * float(line[1])
        credit += float(line[1])
    elif line[2] == 'C0':
        total += 2.0 * float(line[1])
        credit += float(line[1])
    elif line[2] == 'D+':
        total += 1.5 * float(line[1])
        credit += float(line[1])
    elif line[2] == 'D0':
        total += 1.0 * float(line[1])
        credit += float(line[1])

print(f"{total/credit:.6f}")