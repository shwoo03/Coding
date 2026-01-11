loop = int(input())

for _ in range(loop):
    a, b = map(int, input().split())
    print(f"Case #{_ + 1}: {a+b}")

