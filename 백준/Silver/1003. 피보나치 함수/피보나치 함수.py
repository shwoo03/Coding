import math
from collections import deque
import sys
input = sys.stdin.readline


# fibo 함수를 재귀 호출을 할 때 0과 1이 각각 몇 번 출력되는지 구해야 함 
# n 번째 함수는 return 문에서 n-1, n-2를 호출한다.
# 결국 각 count0/1 리스트에서의 점화식 count?[n] = count?[n-1] + count?[n-2] 가 된다.


if __name__ == "__main__":
    count0 = [0] * 41
    count1 = [0] * 41

    count0[0] = 1
    count0[1] = 0
    count1[0] = 0
    count1[1] = 1

    for i in range(2, 41):
        count0[i] = count0[i-1] + count0[i-2]
        count1[i] = count1[i-1] + count1[i-2]
    
    T = int(input())
    for i in range(T):
        index = int(input())
        print(count0[index], count1[index])