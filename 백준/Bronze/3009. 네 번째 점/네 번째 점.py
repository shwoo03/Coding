list_x = []
list_y = []

for i in range(3):
    x, y = map(int,input().split())
    list_x.append(x)
    list_y.append(y)

list_x.sort()
list_y.sort()

if list_x.count(list_x[0]) == 2:
    x = list_x[2]
else:
    x = list_x[0]

if list_y.count(list_y[0]) == 2:
    y = list_y[2]
else:
    y = list_y[0]

print(f"{x} {y}")