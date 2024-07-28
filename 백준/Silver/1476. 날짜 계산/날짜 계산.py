# 준규가 사는 나라는 수 3개를 이용해서 연도를 나타낸다.
# 각각, 지구(E), 태양(S), 달(M)을 나타낸다.
# 각 수는 서로 다른 범위를 가진다. (1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)
# 1년이 지날 때마다, 세 수는 모두 1씩 증가한다.
# 만약, 어떤 수가 범위를 넘어가는 경우에는 1이 된다.
# 예를 들어, 15년은 15 15 15로 나타낼 수 있다.
# 하지만, 1년이 지나서 16년이 지나면 1 16 16이 되고,
# 또 1년이 지나서 1 17 17이 된다.
# E, S, M이 주어졌고 1년이 지났을 때, E, S, M을 구하는 프로그램을 작성하시오.

# 메모리 제한이 4MB 라서 이중 for문을 사용하면 안된다.
# 접근 방식은 1년이 지날 때마다 E, S, M을 1씩 증가시키면서 입력받은 E, S, M과 같아질 때까지 반복한다.

E, S, M = map(int, input().split())
year = 1
while True:
    if (year - E) % 15 == 0 and (year - S) % 28 == 0 and (year - M) % 19 == 0:
        print(year)
        break
    year += 1