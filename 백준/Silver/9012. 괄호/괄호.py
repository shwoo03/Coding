import math
import sys
input = sys.stdin.readline


# VPS 인가??
# stack을 사용해서 할 수 있음  


if __name__ == "__main__":
    T = int(input())

    for i in range(T):
        list_parenthesis = []
        string = input().strip()
        is_vps = True

        for ch in string:
            if ch == '(':
                list_parenthesis.append(ch)
            else:
                if list_parenthesis:
                    list_parenthesis.pop()
                else:
                    is_vps = False
                    break
        
        if list_parenthesis:
            is_vps = False
        
        if is_vps:
            print("YES")
        else:
            print("NO")
