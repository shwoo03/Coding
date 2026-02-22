N = int(input())

list_a = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for i in range(10, 101):
    list_a.append(list_a[i-2] + list_a[i-3])

for _ in range(N):
    a = int(input())
    print(list_a[a-1])
