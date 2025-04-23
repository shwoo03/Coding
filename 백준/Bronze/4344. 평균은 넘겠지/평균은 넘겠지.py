import math
import sys
input = sys.stdin.readline



# 학생 수 N을 받고 C개의 점수를 받음 
# 평균 구해서 평균이 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력 


if __name__ == "__main__":
    T = int(input())
    list_score = []

    for i in range(T):
        data = list(map(int,input().split()))
        list_score.append(data)
    
    for i in range(T):
        total = sum(list_score[i][1:])
        avg = total / list_score[i][0]
        ratio = 0.0
        count = 0

        for score in list_score[i][1:]:
            if score > avg:
                count += 1

        
        ratio = (count / list_score[i][0]) * 100
        print(f"{ratio:.3f}%")  
