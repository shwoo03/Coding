list_alpha = [-1 for i in range(26)]
string = input()

for i,v in enumerate(string):
    index = ord(v) - 97
    if list_alpha[index] == -1:
        list_alpha[index] = i

print(*list_alpha)