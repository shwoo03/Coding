# 그룹 단어란 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.

N = int(input())   
result = 0

for i in range(N):
    word = input()
    is_group = True
    # 중복 문자 체크 변수 
    duplicate_check = []
    
    # 이전 문자 기록 변수
    prev_char = ''
    for ch in word:
        if ch != prev_char:
            if ch in duplicate_check:
                is_group = False
                break
            prev_char = ch
            duplicate_check.append(ch)
        elif ch == prev_char:
            continue
    
    if is_group:
        result += 1

print(result)