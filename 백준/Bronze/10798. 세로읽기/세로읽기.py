list_word = [list(input().strip()) for _ in range(5)]

for j in range(15):
    for i in range(5):
        try:
            print(list_word[i][j], end='')
        except IndexError:
            continue

