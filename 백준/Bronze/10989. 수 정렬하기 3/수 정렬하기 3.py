import math
import sys
input = sys.stdin.readline

# 메모리가 매우 제한됨 
# 카운팅 정렬하면 됨 

if __name__ == "__main__":
    N = int(input())
    list_num = [0] * 10001

    for i in range(N):
        n = int(input())
        list_num[n] += 1
    
    for i in range(10001):
        if list_num[i] != 0:
            for num in range(list_num[i]):
                print(i)
