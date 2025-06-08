import math
import heapq
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline


# 입력되는 문자는 a~z -> 1~26 으로 매핑한다.
#   abba는 -> 1,2,2,1 로 나타낼 수 있다.
#   이러한 과정을 사용해서 충돌이 발생하지 않도록 시그마(a_i * r^i) mod M 을 한다.
#   r = 31, M = 1234567891



if __name__ == "__main__":
    L = int(input())
    word = input().strip()
    result = 0

    r = 31
    M = 1234567891

    for i in range(L):
        char_to_int = ord(word[i]) - ord('a') + 1
        temp = (char_to_int * pow(r, i, M)) % M
        result = (result + temp) % M

    print(result)
