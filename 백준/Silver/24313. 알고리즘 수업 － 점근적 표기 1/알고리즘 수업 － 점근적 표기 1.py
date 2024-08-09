# O(g(n)) = {f(n) | 모든 n ≥ n0에 대하여 f(n) ≤ c × g(n)인 양의 상수 c와 n0가 존재한다}
# 이렇게 정의했을 때, c, n0가 주어질 경우 만족하는지 알아보자 
# 만족하면 1, 아니면 0

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

# a1 - c가 음수일 경우, 모든 n에 대해 성립
if a1 <= c and (a1 * n0 + a0) <= (c * n0):
    print(1)
else:
    print(0)