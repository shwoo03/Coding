N = int(input())
list_num = list(map(int, input().split()))

result = 0
max_result = 0
current_max = list_num[0]

for i in range(1, N):
    if current_max > list_num[i]:
        result += 1
        if result > max_result:
            max_result = result
    else:
        current_max = list_num[i]
        result = 0

print(max_result)