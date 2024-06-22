arr = []
n = int(input())
l = list(map(int,input().split()))
arr = []

l_index = 0
for i in range(n):
    arr.insert(l_index - l[i],i+1)
    l_index += 1

print(*arr)