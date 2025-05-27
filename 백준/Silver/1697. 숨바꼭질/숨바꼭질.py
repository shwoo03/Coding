import math
import heapq
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline


# 점 N(수빈), K(동생)에 존재하고 수빈이는 걷거나 순간이동 가능 
# N의 위치가 X일 때 걸으면 1초 후 x-1 or x+1 로 이동가능 
# 순간 이동하면 1초 후에 2*x의 위치로 이동 
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램 
def bfs(N, K, visited):
    if N == K:
        return 0

    queue = deque()
    queue.append(N)
    visited[N] = True
    dx = [-1, 1, 2]
    count = 0

    while queue:
        for j in range(len(queue)):
            x = queue.popleft()

            for i in range(3):
                if i == 2:
                    nx = x * dx[i]
                else:
                    nx = x + dx[i]
                
                if 0 <= nx <= 100000 and visited[nx] == False:
                    if nx == K:
                        return count + 1
                    queue.append(nx)
                    visited[nx] = True
        
        count += 1



if __name__ == "__main__":
    N, K = map(int,input().split())

    # x - 1, x + 1, 2 * x의 노드를 visited로 처리하고 count 변수를 1개 씩 증가하며 
    #   문제를 해결하면 될듯하다.

    visited = [False] * 100001
    print(bfs(N, K, visited))
