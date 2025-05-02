import math
import sys
input = sys.stdin.readline


# 준규가 가진 동전 종류는 N개
# 동전을 적절히 사용해서 그 가치의 합을 K로 만드려고 한다.
# 동전 개수의 최솟값을 구하는 프로그램 작성 


if __name__ == "__main__":
    N, K = map(int, input().split())
    count = 0

    N_list = []
    for i in range(N):
        N_list.append(int(input()))
    N_list.sort(reverse=True)

    i = 0
    while True:
        count += K // N_list[i]
        K %= N_list[i]

        if K <= 0:
            print(count)
            break
        else:
            i += 1

