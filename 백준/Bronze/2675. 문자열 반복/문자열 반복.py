t = int(input())

for i in range(t):
    r,string = map(str,input().split())
    r = int(r)
    for j in string:
        print(j * r,end="")
    print()