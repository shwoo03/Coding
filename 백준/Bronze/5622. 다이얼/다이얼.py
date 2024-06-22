list_num = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
time = 0

char = input()
for ch in char:
    time += 2
    for i in list_num:
        if ch in i:
            time += (list_num.index(i) + 1)

print(time)