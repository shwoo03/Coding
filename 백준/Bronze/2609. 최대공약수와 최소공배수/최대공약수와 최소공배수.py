import math
import sys
input = sys.stdin.readline

# 두 개의 자연수를 받아서 최대 공약수와 최소 공배수 출력 


if __name__ == "__main__":
    x,y = map(int,input().split())

    print(math.gcd(x,y))
    print(math.lcm(x,y))


