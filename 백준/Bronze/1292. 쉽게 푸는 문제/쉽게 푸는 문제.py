a,b = map(int,input().split())
listNum = []

appendNum = 1
for i in range(1,b+1):
    for n in range(i):
        listNum.append(appendNum)
    appendNum += 1

print(sum(listNum[a-1:b]))