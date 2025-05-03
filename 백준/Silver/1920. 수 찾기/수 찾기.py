import math
import sys
input = sys.stdin.readline


# 주어진 수 안에서 어떤 숫자가 있는지 확인해야 함 
# 해싱을 사용하는 자료형인 set 사용하면 될듯 



if __name__ == "__main__":
    N = int(input())
    nums = set(map(int, input().split()))

    check_n = int(input())
    check_nums = list(map(int, input().split()))

    for num in check_nums:
        if num in nums:
            print(1)
        else:
            print(0)

