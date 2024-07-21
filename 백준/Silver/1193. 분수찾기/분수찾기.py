N = int(input())

diagonal = 1
while N > (diagonal * (diagonal + 1)) // 2:
    diagonal += 1

position_in_diagonal = N - (diagonal * (diagonal - 1)) // 2

if diagonal % 2 == 0:
    numerator = position_in_diagonal
    denominator = diagonal - position_in_diagonal + 1
else:
    numerator = diagonal - position_in_diagonal + 1
    denominator = position_in_diagonal

print(f"{numerator}/{denominator}")


# 시간 초과 ㄷㄷㄷㄷㄷ
# N = int(input())

# line = 0
# repeat = 0

# for i in range(N):
#     repeat += 1
#     if repeat >= line:
#         line += 1
#         repeat = 0
    
#     if line % 2 == 0:
#         a = 1
#         b = line
#         for j in range(repeat):
#             a += 1
#             b -= 1
#     elif line % 2 == 1:
#         a = line
#         b = 1
#         for j in range(repeat):
#             a -= 1
#             b += 1

# print(f'{a}/{b}')