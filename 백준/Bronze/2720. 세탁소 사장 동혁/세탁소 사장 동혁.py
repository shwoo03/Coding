n = int(input())

for i in range(n):
    q = 0
    d = 0
    n = 0
    p = 0
    charge = int(input())
    q = charge // 25
    charge %= 25
    d = charge // 10
    charge %= 10
    n = charge // 5
    charge %= 5
    p = charge // 1
    print(f"{q} {d} {n} {p}")