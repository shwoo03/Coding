import math
import sys
input = sys.stdin.readline


# 은행 대기 줄이 주어지면 최소로 필요한 시간의 합을 구하는 프로그램 작성 


if __name__ == "__main__":
    N = int(input())

    list_time = sorted(map(int, input().split()))
    total = 0
    sum = 0

    for i in list_time:
        sum += i
        total += sum
    
    print(total)
