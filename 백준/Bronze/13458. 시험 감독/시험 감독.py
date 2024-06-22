n = int(input()) # 시험장 개수 
list_a = list(map(int,input().split()))
b,c = map(int,input().split())

result = 0
for i in list_a:
    i -= b
    result += 1
    if i <= 0:
        continue

    result = result + (i // c)
    i %= c
    if i != 0:
        result += 1

print(result)
            