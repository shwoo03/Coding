# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 
# 카드 N개를 가지고 있고, 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지 구하는 프로그램을 작성하시오.

N = int(input())
N_list = list(map(int, input().split()))

M = int(input())
M_list = list(map(int, input().split()))

set_N = set(N_list)

for i in M_list:
    if i in set_N:
        print(1, end=' ')
    else:
        print(0, end=' ')