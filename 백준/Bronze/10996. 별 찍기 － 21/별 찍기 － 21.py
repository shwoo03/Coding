n = int(input())

if n == 1:
    print("*")
else:
    for i in range(n):
        for first in range(0,n,2):
            print("* ",end="")
        print()
        for second in range(1,n,2):
            print(" *",end="")
        print()
        