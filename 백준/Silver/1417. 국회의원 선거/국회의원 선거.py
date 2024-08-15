# 다솜이는 사람의 마음을 읽을 수 있는 기계를 가지고 있는데, 선거 조작을 하려고 한다. ㄷㄷㄷ
# 기계는 각 사람들이 누구를 찍을 지 미리 읽을 수 있다. 
# N 명의 후보가 있고, M 명의 사람의 마음을 읽었다.
# 다솜이는 기호 1번이고, 자신을 찍지 않으려는 사람을 돈으로 매수해서 당선 되려고 한다. 
# 다른 후보들 보다 가장 많은 득표수를 기록하면 당선된다. 

# 매수하는 사람의 최솟값을 출력하는 프로그램 작성 
N = int(input())

votes = []
for i in range(N):
    votes.append(int(input()))

dasom = votes[0]
others = votes[1:]

result = 0

while True:
    others.sort(reverse=True)
    if len(others) == 0 or dasom > others[0]:
        break
    others[0] -= 1
    dasom += 1
    result += 1

print(result)
