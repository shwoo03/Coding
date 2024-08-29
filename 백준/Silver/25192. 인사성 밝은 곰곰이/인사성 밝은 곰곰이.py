# 곰곰티콘을 사용해 인사한다.
# 이를 본 문자열 컬러 임스는 채팅방의 기록을 수집하여 그 중 곰곰티콘이 사용된 횟수를 세려고 한다.
# ENTER는 입장, 기 외는 채팅을 입력한 유저의 닉네임 
# 새로운 사람이 입장한 이후 처음 채팅을 입력하는 사람은 반드시 곰곰티콘으로 인사를 한다.
# 그외의 경우에는 곰곰티콘을 사용하지 않는다.

N = int(input())
chat = []

for i in range(N):
    chat.append(input())

count = 0
check = set()
for i in chat:
    if i == "ENTER":
        check.clear()
    else:
        if i not in check:
            check.add(i)
            count += 1

print(count)