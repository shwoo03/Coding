# 입력: N, M (다리 사이트)
    # 일단 N은 정해져있고 나머지는 나열하면 됨 
    # mCn -> M! / N!(M-N)!

import math

T = int(input())

for i in range(T):
    N, M = map(int, input().split())

    numerator = math.factorial(M)
    denominator = math.factorial(N) * math.factorial(M - N)

    print(numerator // denominator)
