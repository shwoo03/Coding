A, B = map(int,input().split())

result = 0

if B > A:
    A, B = B, A

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

gcd_value = gcd(A, B)
lcm_value = A * B // gcd_value

print(lcm_value)