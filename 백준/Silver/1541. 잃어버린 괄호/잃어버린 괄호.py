import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# 양수와 +, -, 괄호를 가지고 식을 만들었음 
# 괄호를 모두 지웠는데 이후에 이 식의 값을 최소로 만들고 싶음 

# +, - 만 있으므로 -를 기준으로 식을 나누어서 +로 모두 합치고 마지막에 -를 붙이면 됨
# 55 - 50 + 40 이면 55 - (50 + 40) = -35 가 됨 


if __name__ == "__main__":
    s = input().split('-')

    # print(s)   # ['55 ', ' 50 + 40\n']

    # -로 나눈 식을 +로 나누어서 모두 더하기 
    first_group = sum(map(int, s[0].split('+'))) # ['10+20+30', '40+50'] 이면 첫 그룹에서 10, 20, 30 을 더함 
    result = first_group # 첫 그룹의 합을 result에 저장

    for num in s[1:]:
        result -= sum(map(int, num.split('+')))
    
    print(result)



