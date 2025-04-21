import math
import sys
input = sys.stdin.readline





def is_prime(num):
    if num < 2:  
        return 0
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return 0
    return 1



if __name__ == "__main__":
    N = int(input())
    list_num = list(map(int, input().split()))

    result = 0

    for num in list_num:
        result += is_prime(num)
    
    print(result)
