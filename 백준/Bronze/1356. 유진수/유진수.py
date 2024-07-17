N = input()

is_answer = False 

for i in range(1, len(N)):
    str_1 = N[:i]
    str_2 = N[i:]
    
    result1 = 1
    result2 = 1
    
    for j in str_1:
        result1 *= int(j)
    
    for j in str_2:
        result2 *= int(j)
    
    if result1 == result2:
        is_answer = True
        print("YES")
        break

if not is_answer: 
    print("NO")
