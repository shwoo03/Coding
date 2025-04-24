import math
import sys
input = sys.stdin.readline

# 소인수 분해 프로그램 

def get_result(num):
    list_num = []
    i = 2

    while i * i <= num:
        while num % i == 0:
            list_num.append(i)
            num //= i
        
        i += 1

    if num > 1:
        list_num.append(num)
    
    return list_num


        



if __name__ == "__main__":
    N = int(input())

    list_num = get_result(N)
    for num in list_num:
        print(num)



