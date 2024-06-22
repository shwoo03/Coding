list_n = []

for i in range(10):
    n = int(input())
    list_n.append(n%42)

print(len(list(set(list_n))))
