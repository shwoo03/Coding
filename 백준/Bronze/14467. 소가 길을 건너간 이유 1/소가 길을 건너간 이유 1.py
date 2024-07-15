N = int(input())

# 소의 번호를 키로 사용하기 위해 정수형 키 사용
cow_dict = {i: None for i in range(1, 11)}

result = 0 

for i in range(N):
    cow, position = map(int, input().split())
    if cow_dict[cow] is None:
        cow_dict[cow] = position
    elif cow_dict[cow] != position:
        cow_dict[cow] = position
        result += 1

print(result)