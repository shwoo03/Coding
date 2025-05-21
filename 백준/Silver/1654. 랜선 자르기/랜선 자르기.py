import math
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline



# K개의 랜선을 이미 가지고 있고, 여기서 N개의 랜선을 만들려고 한다.
# cm 단위로 정수 길이만큼 자른다. 최대 랜선의 길이를 구하시오 
# 1. 중간 값을 나누고 탐색 시작 
# 2. K개가 만족이 되는 것과 아닌 2가지 경우를 나누고 계속 탐색 
# 3. 출력 


def binary_search(K, N, list_lan):
    start = 1
    end = list_lan[-1]
    result = 0

    while start <= end:
        mid = (start + end) // 2
        sum_lan = 0
        for lan in list_lan:
            sum_lan += lan // mid
        
        if sum_lan < N:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    
    return result 




if __name__ == "__main__":
    K, N = map(int,input().split())
    list_lan = []
    for i in range(K):
        list_lan.append(int(input()))
    list_lan.sort()
    
    result = binary_search(K, N, list_lan)
    print(result)
