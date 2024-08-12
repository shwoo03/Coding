# 폴리오미노 2개를 무한개만큼 가지고 있다. 
# AAAA 와 BB 
# . 와 X 로 이루어진 보드가 있을 때, X 를 모두 폴리오미노로 덮으려고 한다.
# 단, . 은 덮으면 안된다. 
# 첫째 줄에 보드판이 주어진다. 보드판의 크기는 최대 50이다. 
# 사전 순으로 가장 앞서는 답을 출력한다. 만약 덮을 수 없으면 -1을 출력한다. 

board = input()

result = []
i = 0
n = len(board)

while i < n:
    if board[i] == '.':
        result.append('.')
        i += 1
        continue
    
    start = i
    while i < n and board[i] == 'X':
        i += 1
    
    length = i - start
    
    if length % 2 != 0:
        print(-1)
        exit()
    
    result.append('A' * (length // 4 * 4))
    result.append('B' * ((length % 4) // 2 * 2))

print(''.join(result))
