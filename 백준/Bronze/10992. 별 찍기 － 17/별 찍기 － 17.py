n = int(input())

for i in range(0,n-1,1):
    if i == 0:
        print(" " * (n-i-1) + "*" + " " * (2*i-1))
    else:
        print(" " * (n-i-1) + "*" + " " * (2*i-1) + "*")

print("*" * (2*n-1))