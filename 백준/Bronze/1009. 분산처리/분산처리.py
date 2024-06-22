t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    a_last_digit = a % 10

    # 거듭제곱 결과의 주기는 최대 4
    b %= 4

    # 거듭제곱의 주기가 0일 경우 주기를 4로 변경
    b = 4 if b == 0 else b

    # 주기 내에서 계산된 거듭제곱 결과의 마지막 자리 숫자
    result = (a_last_digit ** b) % 10

    # 결과가 0인 경우 10으로 출력
    print(result if result != 0 else 10)