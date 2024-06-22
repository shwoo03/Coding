n = int(input())
list_cup = [i for i in range(3)]

for i in range(n):
    a,b = map(int,input().split())
    list_cup[a-1] , list_cup[b-1] = list_cup[b-1] , list_cup[a-1]

print(list_cup.index(0)+1)