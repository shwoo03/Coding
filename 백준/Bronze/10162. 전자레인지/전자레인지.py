n = int(input())

m5 = 0
m1 = 0
s10 = 0

if n % 10 != 0:
    print(-1)
else:
    m5 += n // 300
    n %= 300
    m1 += n // 60
    n %= 60
    s10 += n // 10
    n %= 10
    print(f"{m5} {m1} {s10}")

