# 0, 1 로만 이루어진 문자열 S를 입력받아 0과 1의 개수가 같아지도록 뒤집어서 출력하는 프로그램을 작성하라.
# 단, 1번 뒤집을 때는 연속된 0 또는 1을 모두 뒤집는다.

S = input()

# 결과 문자열을 저장할 변수 초기화
result = S[0]

# 문자열을 순회하면서 연속된 문자를 하나로 압축
for i in range(1, len(S)):
    if S[i] != S[i - 1]:
        result += S[i]

zero = 0
one = 0
for i in result:
    if i == '0':
        zero += 1
    else:
        one += 1

print(min(zero, one))