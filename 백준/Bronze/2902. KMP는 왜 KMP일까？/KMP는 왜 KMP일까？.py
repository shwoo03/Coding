ch = input()
list_ch = []

for i in ch:
    if i.isupper():
        list_ch.append(i)

for i in list_ch:
    print(i,end="")