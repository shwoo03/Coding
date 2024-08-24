# 정수가 하나 적혀있는 카드 N 개를 가지고 있다.
# 정수 M개가 주어졌을 때, 이 수가 적혀있는 카드를 몇개 가지고 있는지 구하는 프로그램 작성 

import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))

M = int(input())
find = list(map(int, input().split()))

count_dict = {}
for card in cards:
    if card in count_dict:
        count_dict[card] += 1
    else:
        count_dict[card] = 1

for num in find:
    print(count_dict.get(num, 0), end=' ')
