import math
from collections import deque
import sys
input = sys.stdin.readline


# 1번 카드가 제일 위에 있고 카드 한 장이 남을 때 까지 
# 1. 제일 위의 카드릴 바닥에 버린다. 
# 2. 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다. 


if __name__ == "__main__":
    N = int(input())
    card_queue = deque(range(1, N + 1))

    while len(card_queue) > 1:
        card_queue.popleft()         
        card_queue.append(card_queue.popleft())  

    print(card_queue[0])
