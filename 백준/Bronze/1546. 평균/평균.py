import math
import sys
input = sys.stdin.readline



# 수 받고 최대값 찾아서 모든 값에 n/M*100 해주고 평균 구하기



if __name__ == "__main__":
    N = int(input())

    list_num = list(map(int, input().split()))

    list_num.sort()
    max_num = list_num[-1]

    new_score = []
    for num in list_num:
        new_score.append(num/max_num*100)
    
    print((sum(new_score)) / N)