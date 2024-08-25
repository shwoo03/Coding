# 어떤 문자열이 주어지면, 관호들의 균형이 잘 맞춰져 있는지 확인하는 프로그램 작성 
# 모든 왼쪽 소괄호는 오른쪽 소괄호와만 짝을 이룬다.
# 모든 왼쪽 대괄호는 오른쪽 대괄호와만 짝을 이룬다.
# 모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
# 모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
# 짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다. 
# " ." 와 같이 괄호가 하나도 없는 경우도 균형잡힌 문자열로 간주할 수 있다. 

# 각 줄마다 해당 문자열이 균형을 이루면 yes 아니면 no 출력 

import sys

input = sys.stdin.readline
list_s = []

while True:
    s = input().rstrip()
    if s == '.':
        break
    list_s.append(s)

for s in list_s:
    stack = []
    check = True
    
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] == '[':
                check = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] == '(':
                check = False
                break
            elif stack[-1] == '[':
                stack.pop()
    if check and not stack:
        print('yes')
    else:
        print('no')