# N,M이 주어지면, 길이가 M인 수열을 모두 구하는 프로그램 
# 1부터 N까지의 자연수 중에서 중복 없이 M개 
# 오름차순 

from itertools import combinations

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]

result = list(combinations(arr, M))
for i in result:
    print(*i)