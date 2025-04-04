# N과 M이 주어졌을 때 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 n까지 자연수 중에서 중복 없이 m개를 고른 수열
# 1. 오름차순 으로 정렬되어야 한다
# 2. 한 줄에 하나 씩 문제의 조건을 만족하는 수열을 출력한다
# 3. 각 수열은 공백으로 구분한다

N, M = map(int, input().split())

# 음.. 순열을 구해서 출력해야 하는데 
# intertools 모듈을 사용하면 편할 것 같음

from itertools import permutations

for p in permutations(range(1, N+1), M):
    print(*p)
