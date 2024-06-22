ch = input()
list_ch = []

for i in ch:
    if i.islower() == True:
        list_ch.append(i.upper())
    else:
        list_ch.append(i.lower())

print(''.join(list_ch))