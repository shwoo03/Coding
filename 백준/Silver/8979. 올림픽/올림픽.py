# 올림픽에서 금,은,동 메달이 주어지면 다음 다음 규칙에 따라서 순위를 결정한다.
# 1. 금메달 개수가 많은 나라
# 2. 금메달 개수가 같으면 은메달 개수가 많은 나라
# 3. 금, 은메달 개수가 같으면 동메달 개수가 많은 나라

# 각 국가는 1부터 N 사이의 정수로 표현된다.
# 등수는 자신보다 더 잘한 나라 수 + 1로 정의된다.
# 금, 은, 동이 모두 같다면 등수는 같다.
# 예를 들어 4개의 국가가 있고, 2등이 등수가 같다면 1,2,2,4 등으로 된다. 

N, k = map(int, input().split())

list_medal = []
for i in range(N):
    list_medal.append(list(map(int, input().split())))

sorted_medal = sorted(list_medal, key=lambda x: (x[1], x[2], x[3]), reverse=True)
rank = 0
rank_dict = {sorted_medal[0][0]: rank} 

for i in range(1, N):
    if sorted_medal[i][1:] == sorted_medal[i - 1][1:]:
        rank_dict[sorted_medal[i][0]] = rank
    else:
        rank = i + 1
        rank_dict[sorted_medal[i][0]] = rank

print(rank_dict[k])