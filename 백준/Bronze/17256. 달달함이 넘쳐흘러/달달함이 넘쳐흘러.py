# 입력값을 받습니다.
a_x, a_y, a_z = map(int, input().split())
c_x, c_y, c_z = map(int, input().split())

# b의 값을 계산합니다.
b_x = c_x - a_z
b_y = c_y // a_y  # c_y는 a_y의 배수이므로 나누어 떨어질 것이라고 가정합니다.
b_z = c_z - a_x

# 결과를 출력합니다.
print(b_x, b_y, b_z)
