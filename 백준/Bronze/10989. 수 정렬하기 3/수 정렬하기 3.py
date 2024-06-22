# 메모리 제한이 걸려있는 문제다 
# for 문으로 list에 append 사용하면 메모리 재할당이 
# 이루어져서 메모리를 효율적으로 사용못한다. 
# 따라서 10001 만큼의 리스트를 만들고 각 요소마다 0 을 할당 
# 그 후 0보다 큰 요소를 갖는 인덱스들을 찾아서 출력 

import sys

n = int(sys.stdin.readline())
list_num = [0] * 10001

for _ in range(n):
    list_num[int(sys.stdin.readline())] += 1

for i in range(10001):
    if list_num[i] != 0:
        for j in range(list_num[i]):
            print(i)