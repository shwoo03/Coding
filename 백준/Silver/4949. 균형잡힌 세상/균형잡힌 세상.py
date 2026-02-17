strings = []
stack = []

while True:
    temp = input()

    if temp == ".":
        break
    else:
        strings.append(temp)

for string in strings:
    # 아 코드 이상한데 ;;;; 그냥 할래 
    stack = []
    for char in string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if len(stack) == 0:
                print("no")
                break
            else:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    print("no")
                    break
        elif char == "[":
            stack.append(char)
        elif char == "]":
            if len(stack) == 0:
                print("no")
                break
            else:
                if stack[-1] == "[":
                    stack.pop()
                else:
                    print("no")
                    break
    else:
        if len(stack) == 0:
            print("yes")
        else:
            print("no")

