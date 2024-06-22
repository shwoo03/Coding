while True:
    result = 0
    ch = input()
    if ch == '#':
        break
    for c in ch:
        if c in "aeiouAEIUO":
            result +=1
        else:
            pass
    print(result)