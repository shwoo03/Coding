import math
from collections import deque
import sys
input = sys.stdin.readline


# W, B에 따라서 적절하게 체스판 칠하기 


if __name__ == "__main__":
    N, M = map(int,input().split())
    map_list = []
    min_result = 1000000

    for i in range(N):
        map_list.append(list(input().strip()))  
    
    for row in range(N - 7):  
        for col in range(M - 7):  
            w_start_cnt = 0  
            b_start_cnt = 0  

            for i in range(8):  
                for j in range(8):  
                    current = map_list[row + i][col + j]
                    if (i + j) % 2 == 0:
                        if current != 'W':
                            w_start_cnt += 1
                        if current != 'B':
                            b_start_cnt += 1
                    else:
                        if current != 'B':
                            w_start_cnt += 1
                        if current != 'W':
                            b_start_cnt += 1

            min_result = min(min_result, w_start_cnt, b_start_cnt)

    print(min_result)

