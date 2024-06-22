n = int(input())

while(n):
    try:
        a,b = map(int,input().split(","))
        print(a+b)
    except EOFError:
        break
