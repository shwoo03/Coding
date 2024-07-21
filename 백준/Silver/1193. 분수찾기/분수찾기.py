def find_fraction(X):
    # X번째 대각선이 몇 번째인지 찾기
    diagonal = 1
    while X > (diagonal * (diagonal + 1)) // 2:
        diagonal += 1
    
    # X번째 대각선에서의 위치 찾기
    position_in_diagonal = X - (diagonal * (diagonal - 1)) // 2
    
    if diagonal % 2 == 0:
        numerator = position_in_diagonal
        denominator = diagonal - position_in_diagonal + 1
    else:
        numerator = diagonal - position_in_diagonal + 1
        denominator = position_in_diagonal
    
    return f"{numerator}/{denominator}"

# 예제 입력
N = int(input())

# 결과 출력
fraction = find_fraction(N)
print(fraction)