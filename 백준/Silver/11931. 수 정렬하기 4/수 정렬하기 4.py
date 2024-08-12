# N개의 수가 주어졌을 때, 이것을 내림차순으로 정렬하는 프로그램 작성 

import sys
input = sys.stdin.read

data = input().split()


N = int(data[0])
num = list(map(int, data[1:]))

num.sort(reverse=True)

for number in num:
    print(number)