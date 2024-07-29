# 길이가 64cm 인 막대를 가지고 있다.
# 길이가 X인 막대를 만드려고 하는데, 잘라서 붙이는 것만으로 만들 수 있다.

# 1. 지민이가 가지고 있는 막대의 길이를 모두 더한다. 처음은 64cm 하나만 가진다.
# 2. 만약 더한 길이가 X보다 크다면, 아래와 같은 과정을 반복한다.
# 2-1. 가지고 있는 막대 중 길이가 가장 짧은 것을 절반으로 자른다.
# 2-2. 만약 가지고 있는 막대의 절반 중 하나를 버리고 남은 막대의 길이의 합이 X보다 크거나 같으면, 자른 막대의 절반 중 하나를 버린다. 
# 2-3. 이제 남은 모든 막대를 풀어서 X만큼의 길이를 만든다.

X = int(input())

result = [64]

while True:
    if sum(result) == X:
        print(len(result))
        break
    elif sum(result) > X:
        temp = result.pop()
        temp = temp // 2
        result.append(temp)
    else:
        result.append(result[-1] // 2)
