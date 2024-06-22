t = int(input())

for i in range(t):
    list_ch = list(map(str,input().split()))
    num = float(list_ch[0])
    for n in list_ch:
        if n == '@':
            num *= 3
        elif n == '%':
            num += 5
        elif n == '#':
            num -= 7
        else:
            continue
    print(f"{num:.2f}")
    
    