# 재민이는 돈을 관리하고 있다. 
# 근데 실수가 많아서 수를 부를 때마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 된다. 
# 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다. 

K = int(input())
stack = []

for _ in range(K):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))