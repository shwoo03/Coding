# 서로 다른 N 개의 자연수의 합이 S라고 한다. 
# S를 알 때, 자연수 N의 최댓값은 얼마인가?

# N*(N+1)/2 <= S
# N = -1 + sqrt(1+8S) / 2

S = int(input())
print(int((-1 + (1+8*S)**0.5) / 2))