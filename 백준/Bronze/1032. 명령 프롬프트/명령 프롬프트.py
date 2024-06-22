n = int(input())

result = input()
for _ in range(n-1):
    temp = ""
    file_name = input()
    for i in range(len(result)):
        if file_name[i] == result[i]:
            temp += result[i]
        else:
            temp += '?'
    result = temp

print(result)