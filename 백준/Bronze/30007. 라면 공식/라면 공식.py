N = int(input())

for i in range(N):
    ai, bi, xi = map(int, input().split())
    print(ai*(xi-1)+bi)