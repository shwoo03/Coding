N, P = map(int, input().split())

set_num = set()
sequence = []
remain = N

while remain not in set_num:
    set_num.add(remain)
    sequence.append(remain)
    remain = (remain * N) % P

# 반복되는 부분의 길이 계산
repeating_start = sequence.index(remain)
repeating_length = len(sequence) - repeating_start

print(repeating_length)
