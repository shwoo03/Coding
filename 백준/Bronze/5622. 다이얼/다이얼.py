# 기본 2초 (다이얼 1) + 추가 1초 (다이얼 2~9)
alpha_list = [[0], [0], [0], ['A','B','C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'],
         ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]

get_input = list(input())
# print(get_input) -> WA == ['W', 'A']

result = 0
for ch in get_input:
    result += alpha_list.index([i for i in alpha_list if ch in i][0])

print(result)