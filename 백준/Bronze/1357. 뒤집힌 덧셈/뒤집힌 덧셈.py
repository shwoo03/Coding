x, y = map(int, input().split())

result = int(str(x)[::-1]) + int(str(y)[::-1])
print(int(str(result)[::-1]))