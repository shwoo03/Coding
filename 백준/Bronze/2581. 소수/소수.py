m = int(input())
n = int(input())
list_prime = []

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for x in range(m,n+1,1):
    if is_prime(x):
        list_prime.append(x)

if not list_prime:
    print(-1)
else:
    print(sum(list_prime))
    print(min(list_prime))