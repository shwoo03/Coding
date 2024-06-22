count = 1

while True:
    L,P,V = map(int,input().split())
    if L == 0 and P == 0 and V == 0:
        break
    else:
        result = (V // P) * L + min((V % P), L)
        print(f"Case {count}: {result}")
        count += 1
