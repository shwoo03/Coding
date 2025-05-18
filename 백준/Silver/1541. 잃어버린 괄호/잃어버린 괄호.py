import math
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline


# +, -, ()를 가지고 식을 만들었다.
# 그리고 괄호를 모두 지움 괄호를 쳐서 식의 값을 최소로 만들어야 한다.
# 10 + 20 - 20 + 10 + 20 - 20 이런식이면 
# -를 기준으로 뒤에 있는 덧셈을 먼저 하면 최대로 뺄 수 있음 
# 여기서 첫 요소를 제외한 모든 나머지 항들은 - 항이므로 쉽게 계산 가능 

if __name__ == "__main__":
    expression = input().strip().split("-")
    positive = sum(map(int, expression[0].split("+")))
    negative = expression[1:]
    sum_negative = 0
    for nums in negative:
        sum_negative += sum(map(int, nums.split("+")))
    
    print(positive - sum_negative)

