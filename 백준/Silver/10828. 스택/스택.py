import math
import sys
input = sys.stdin.readline





if __name__ == "__main__":
    list_stack = []
    n = int(input())
    output = []

    for _ in range(n):
        words = input().split()

        if words[0] == "push":
            list_stack.append(words[1])
        elif words[0] == "pop":
            if list_stack:
                output.append(list_stack.pop())
            else:
                output.append("-1")
        elif words[0] == "size":
            output.append(str(len(list_stack)))
        elif words[0] == "empty":
            output.append("1" if not list_stack else "0")
        elif words[0] == "top":
            if list_stack:
                output.append(list_stack[-1])
            else:
                output.append("-1")

    for result in output:
        print(result)
