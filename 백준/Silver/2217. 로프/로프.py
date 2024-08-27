# N개의 로프가 있고 각각의 로프는 굵기나 길이가 다르다.
# 로프로 이런저런 물체를 올릴 수 있다. 또한, 각각의 로프는 최대 중량이 있다.
# 이 로프들을 병렬로 연결하면 각각의 로프에 걸리는 중량을 나눌 수 있다.
# k 개의 로프를 사용해서 w인 물체를 들어올리면, 각 로프에는 w/k만큼의 중량이 걸리게 된다.
# 로프의 정보가 주어지면, 이 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구하는 프로그램을 작성하시오.
# 단, 로프를 모두 사용하지 않아도 된다.

N = int(input())
rope = []

for i in range(N):
    rope.append(int(input()))

rope.sort()

max_weight = 0

for i in range(N):
    weight = rope[i] * (N - i)
    if weight > max_weight:
        max_weight = weight

print(max_weight)