# N 개의 정수가 주어졌을 때, 안에 X라는 정수가 존재하는지 알아내는 프로그램 작성 
# 존재하면 1, 안하면 0 

import sys

input = sys.stdin.readline
N = int(input())
A = set(map(int, input().split())) 

M = int(input())
B = list(map(int, input().split()))

for num in B:
    if num in A:
        print(1)
    else:
        print(0)


# 정보!
# list는 모든 요소를 순차탐색 하는데 
# set은 해시테이블을 사용하기 때문에 O(1)에 탐색 가능하다.