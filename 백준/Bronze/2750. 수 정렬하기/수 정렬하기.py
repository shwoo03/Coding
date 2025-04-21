import math
import sys
input = sys.stdin.readline







if __name__ == "__main__":
    N = int(input())

    list_num = []
    for i in range(N):
        list_num.append(int(input()))

    list_num.sort()
    for num in list_num:
        print(num)