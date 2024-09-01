# 어떤 문제의 난이도는 그 문제를 푼 사람들이 제출한 난이도 의견을 바탕으로 결정한다. 
# 난이도 의견은 그 사용자가 생각한 난이도를 의미하는 정수 하나로 주어진다. solved.ac가 사용자들의 의견을 바탕으로 난이도를 결정하는 방식은 다음과 같다.
# 아직 아무 의견이 없다면 문제의 난이도는 0으로 결정한다.
# 의견이 하나 이상 있다면, 문제의 난이도는 모든 사람의 난이도 의견의 30% 절사평균으로 결정한다.

# 여기서는 30% 절사평균인데, 상위 15%와 하위 15%를 제외한 나머지 70%의 평균을 의미한다.
# 제외되는 사람의 수는 위, 아래에서 각각 반올림한다. 25명이 투표한 경우 위, 아래에서 각각 3.75명을 제외해야 하는데, 이 경우 반올림해 4명씩을 제외한다.
# 마지막으로, 계산된 평균도 정수로 반올림된다. 절사평균이 16.7이었다면 최종 난이도는 17이 된다.
import sys
import math

input = sys.stdin.read
data = input().split()


N = int(data[0])
arr = list(map(int, data[1:]))

if N == 0:
    print(0)
else:
    arr.sort()
    
    trim_count = int(N * 0.15 + 0.5)  

    trimmed_arr = arr[trim_count:N - trim_count]
    
    trimmed_mean = sum(trimmed_arr) / len(trimmed_arr)

    if trimmed_mean - int(trimmed_mean) >= 0.5:
        trimmed_mean = int(trimmed_mean) + 1
    else:
        trimmed_mean = int(trimmed_mean)

    print(trimmed_mean)

