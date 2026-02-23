N = int(input())

fact = 1
for i in range(1, N + 1):
    fact *= i

str_fact = str(fact)
count = 0
for char in reversed(str_fact):
    if char == '0':
        count += 1
    else:
        break  

print(count)