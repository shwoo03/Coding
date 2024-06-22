result = 0

for i in range(4):
    odd = input()
    even = input()
    for odd_line in range(0,8,2):
        if odd[odd_line] == 'F':
            result += 1
    
    for even_line in range(1,8,2):
        if even[even_line] == 'F':
            result += 1

print(result)

