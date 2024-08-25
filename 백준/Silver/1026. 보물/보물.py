# 길이가 N인 정수 배열 A와 B가 있다.
# 함수 S를 정의하면 S = A[0]*B[0] + A[1]*B[1] + ... + A[N-1]*B[N-1]이다.
# S의 값을 가장 작게 만들기 위한 A의 순서를 구하라.
# 단, B에 있는 수는 재배열하면 안된다.
# S의 최솟값을 출력하는 프로그램을 작성하시오.

import sys 
input = sys.stdin.readline

N = int(input())
list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))

list_A.sort()
list_B.sort(reverse=True)
sum = 0

for i in range(N):
    sum += list_A[i] * list_B[i]

print(sum)