# S = A[0] * B[0] + ... + A[N-1] * B[N-1]
    # S의 값을 가장 작게 만들기 위해 A의 수를 재배열 해야한다. 단, B는 건들이면 안된다.
    # 입력: N, A배열, B배열 
    # 출력: S의 최솟값 

'''
    A배열은 오름차순 B 배열은 내림차순으로 정렬해서 각각의 원소를 곱하면 S의 최솟값이 될 것임 
'''

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

S = 0
for i in range(N):
    S += A[i] * B[i]

print(S)