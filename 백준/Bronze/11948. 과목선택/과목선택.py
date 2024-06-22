list_s = []

for i in range(4):
    list_s.append(int(input()))

list_2 = []
for i in range(2):
    list_2.append(int(input()))

sum = sum(list_s) - min(list_s)
sum += max(list_2)
print(sum)