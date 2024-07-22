N = int(input())

list_DB = []

for i in range(N):
    age, name = input().split()
    
    list_DB.append((int(age), name))

list_DB.sort(key = lambda x: x[0])

for i in list_DB:
    print(i[0], i[1])