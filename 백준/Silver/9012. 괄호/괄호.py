# 괄호 문자열은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있다.
# 그 중 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열이라고 부른다. 
# 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다.
# 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다.
# 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다.
# 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어라.

N = int(input())

# ( 괄호를 stack에 넣고 ) 괄호를 만나면 stack에서 pop
# stack이 비어있으면 NO, stack이 비어있지 않고 모든 괄호를 pop했으면 YES 
for i in range(N):
    stack = []
    data = input().strip()
    
    for d in data:
        if d == '(':
            stack.append(d)
        else:
            if not stack:
                print('NO')
                break
            stack.pop()
    else:
        if not stack:
            print('YES')
        else:
            print('NO')