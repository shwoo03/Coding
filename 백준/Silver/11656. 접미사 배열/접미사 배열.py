
# 접미사 배열은 문자열 S의 모든 접미사를 사전순으로 정렬해 놓은 배열이다.
# baekjoon의 접미사는 baekjoon, aekjoon, ekjoon, kjoon, joon, oon, on, n이다.
# 이를 사전수으로 정렬하면, aekjoon, baekjoon, ekjoon, joon, kjoon, n, on, oon이다.
# 문자열 S가 주어졌을 때, 모든 접미사를 사전순으로 정렬한 다음 출력하는 프로그램을 작성하시오.

import sys 
input = sys.stdin.readline

S = input().strip()
suffix = []

for i in range(len(S)):
    suffix.append(S[i:])

suffix.sort()
for s in suffix:
    print(s)