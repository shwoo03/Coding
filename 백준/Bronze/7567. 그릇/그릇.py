ch = input()
result = 10

for i in range(0,len(ch)-1):
    if ch[i] == '(':
        if ch[i+1] == '(':
            result += 5
        elif ch[i+1] == ')':
            result += 10
    elif ch[i] == ')':
        if ch[i+1] == '(':
            result += 10
        elif ch[i+1] == ')':
            result += 5

print(result) 

    
