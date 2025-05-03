import math
import sys
input = sys.stdin.readline



# 0이 들어오면 하나씩 빼면 됨 


if __name__ == "__main__":
    K = int(input())
    list_num = []

    for i in range(K):
        n = int(input())

        if n == 0:
            if list_num:
                list_num.pop()
            else:
                continue
        else:
            list_num.append(n)

    sum = 0
    for num in list_num:
        sum += num
    
    print(sum)

