import math
import sys
input = sys.stdin.readline



# M 이상 N 이하의 소수를 모두 출력하는 프로그램 작성 

def is_prime(x):
    if x < 2:
        return False
    
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    
    return True


if __name__ == "__main__":
    M, N = map(int, input().split())

    for num in range(M, N+1):
        if is_prime(num):
            print(num)
