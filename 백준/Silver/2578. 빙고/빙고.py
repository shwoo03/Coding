# 빙고 게임은 다음과 같은 방식으로 이루어짐. 
# 5 x 5 킈의 빙고판에 1 부터 25 까지의 자연수를 중복없이 하나씩 적음
# 1 부터 25 까지의 자연수를 중복없이 하나씩 순서대로 부름
# 차례대로 지우다가 같은 가로줄, 세로줄, 또는 대각선 위에 있는 5개의 수를 지우고,
# 그것이 3개의 빙고줄 이상이 되는 순간 빙고 외치고 끝냄 

# 빙고판의 수와 사회자가 부르는 수의 순서가 주어질 때,
# 몇 번째 수를 부르면 철수가 빙고를 외치는지 출력하는 프로그램 작성 

def check_bingo(board):
    line_count = 0

    for i in range(5):
        if sum(board[i]) == 0:
            line_count += 1

    for i in range(5):
        if sum(board[j][i] for j in range(5)) == 0:
            line_count += 1

    if sum(board[i][i] for i in range(5)) == 0:
        line_count += 1
    if sum(board[i][4 - i] for i in range(5)) == 0:
        line_count += 1

    return line_count


list_bingo = []
for i in range(5):
    list_bingo.append(list(map(int, input().split())))

list_call = []
for i in range(5):
    list_call += list(map(int, input().split()))

count = 0  
line = 0  


for item in list_call:
    count += 1  

    for i in range(5):
        if item in list_bingo[i]:
            idx = list_bingo[i].index(item)
            list_bingo[i][idx] = 0
            break

    line = check_bingo(list_bingo)

    if line >= 3:
        print(count)
        break
