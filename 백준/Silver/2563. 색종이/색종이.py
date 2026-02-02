list_do = [[0 for i in range(100)] for j in range(100)]

N = int(input())

for a in range(N):
    x, y = map(int, input().split())

    for x1 in range(x, x + 10):
        for y1 in range(y, y + 10):
            list_do[x1][y1] = 1

result = 0
for row in list_do:
    result += row.count(1)

print(result)
