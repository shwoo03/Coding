board = [list(input().ljust(15,' ')) for _ in range(5)]
result = ''

for j in range(15):
    for i in range(5):
        if board[i][j] != ' ':
            result += board[i][j]

print(result)