def bino_coef(n, r):
    cache = [[0 for _ in range(r+1)] for _ in range(n+1)]

    for i in range(n+1):
        cache[i][0] = 1
    for i in range(r+1):
        cache[i][i] = 1

    for i in range(1, n+1):
        for j in range(1, r+1):
            cache[i][j] = cache[i-1][j] + cache[i-1][j-1]

    return cache[n][r]

n,k = map(int,input().split())
result = bino_coef(n,k)

print(result)
