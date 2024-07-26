N = int(input())

result = 0
i = 5

while N // i > 0:
    result += N // i
    i *= 5

print(result)