T = int(input())

for i in range(T):
    n = input()
    if len(n) >= 6 and len(n) <= 9:
        print("yes")
    else:
        print("no")