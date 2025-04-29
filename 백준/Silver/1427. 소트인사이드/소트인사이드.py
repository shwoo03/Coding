import math
import sys
input = sys.stdin.readline


# 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정리하기 


if __name__ == "__main__":
    num = input().strip()
    num_list = list(map(int, num))
    num_list.sort(reverse=True)

    for n in num_list:
        print(n,end='')