ch = input()
n = 16

result = 0 
x = 0
for i in ch[::-1]:
    if i in "ABCDEFZ":
        result += (ord(i) - 65 + 10)  * (n ** x)
    else:
        result += int(i) * (n ** x)
    x += 1 

print(result)
