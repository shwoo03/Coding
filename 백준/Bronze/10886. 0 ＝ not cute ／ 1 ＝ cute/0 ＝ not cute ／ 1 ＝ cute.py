k = int(input())

v1 = 0
v0 = 0
for i in range(k):
    n = int(input())
    if n == 1:
        v1 += 1
    else:
        v0 += 1

if v1 > v0:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!");    