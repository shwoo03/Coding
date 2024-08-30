# 게임에는 총 N개의 레벨이 있고, 각 레벨을 클리어하면 보상을 받을 수 있습니다.
# 점수는 레벨을 클리어하면서 얻은 점수의 합으로, 이점수를 바탕으로 온라인 순위를 매깁니다.
# 레벨을 난이도 순으로 배치했지만, 쉬운 레벨이 어려운 레벨보다 점수를 많이 받는 실수를 했다.
# 문제를 해결하기 위해서 특정 레벨의 점수를 감소시키려고 한다.
# 각 레벨을 클리어하면서 얻는 점수가 증가하게 만드려고 한다.

# 각 레벨을 클리어하는 점수가 주어지면, 몇 번 감소시키면 되는지 구하는 프로그램을 작성하세요 
# 점수는 항상 양수이고, 1만큼 감소시키는 것이 1번이다. 
# 답이 여러 가지인 경우에는 가장 작은 값을 출력하세요.

N = int(input())
score = []

for i in range(N):
    score.append(int(input()))

count = 0
for index in range(N - 1, 0, -1):
    if score[index] <= score[index - 1]:
        difference = score[index - 1] - score[index] + 1
        count += difference
        score[index - 1] -= difference

print(count)