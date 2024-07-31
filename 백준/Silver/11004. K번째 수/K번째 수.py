# 수 N개 A1,A2,...,AN 이 주어진다.
# 오름차순으로 정렬했을 때, 앞에서부터 K번째 있는 수를 구하세요 

N,K = map(int,input().split())

A = list(map(int,input().split()))
A.sort(reverse=False)

print(A[K-1])