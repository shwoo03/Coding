import math

N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    
    print(math.factorial(b) // (math.factorial(a) * math.factorial(b - a)))