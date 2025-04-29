import math
import sys
input = sys.stdin.readline


# 666 들어간 종말 수 찾기 


if __name__ == "__main__":
    N = int(input())
    if N == 1:
        print("666")
    elif N == 2:
        print("1666")
    else:
        count = 2
        num = 2665

        while True:
            num += 1
            if "666" in str(num):
                count += 1
                if count == N:
                    print(num)
                    break
