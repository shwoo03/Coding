# 방 번호를 붙이려고 하는데 0 부터 9 까지 숫자가 하나씩 들어있다. 
# 방 번호가 주어졌을 때, 필요한 세트의 수를 구하시오 
# 단, 6과 9는 같이 사용할 수 있다.


room_number = input().strip()
counts = [0] * 10

for char in room_number:
    counts[int(char)] += 1

combined_six_nine = (counts[6] + counts[9] + 1) // 2
counts[6] = counts[9] = combined_six_nine

required_sets = max(counts)
print(required_sets)
