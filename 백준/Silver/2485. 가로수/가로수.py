# 가로수가 모두 같은 간격이 되도록 가로수를 추가로 심는 작업 
# 가장 적은 수의 나무를 심는다.
# 1,3,7,13 이면 5,9,11의 위치에 가로수를 심으면 된다. 
# 2,6,12,18 이면 4,8,10,14,16의 위치에 가로수를 심으면 된다.
# 나무는 기존 나무들 사이에만 심을 수 있다. 
import sys 
import math
from functools import reduce
input = sys.stdin.readline

def gcd_multiple(numbers):
    return reduce(math.gcd, numbers)

N = int(input())
list_tree = []

for i in range(N):
    list_tree.append(int(input()))

list_tree.sort()

# 가로수 사이의 간격의 최대공약수를 구하면 됨 
list_space = []
for i in range(1, N):
    list_space.append(list_tree[i] - list_tree[i-1])

gcd = gcd_multiple(list_space)

count = 0
for i in range(1, N):
    count += (list_tree[i] - list_tree[i-1]) // gcd - 1

print(count)
