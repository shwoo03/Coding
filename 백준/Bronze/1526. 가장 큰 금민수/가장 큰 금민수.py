N = int(input())

for i in range(N,0,-1):
    if all(char in '47' for char in i.__str__()):
        print(i)
        break
    else:
        continue

