n = int(input())

if n <= 5:
    print(n)
else:
    n -= 5
    if (n // 4) % 2 == 0:
        print(5 - (n % 4))
    else:
        print((n % 4 + 1))