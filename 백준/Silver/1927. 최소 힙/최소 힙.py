import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# 최소 힙 라이브러리 사용 
import heapq as hq

# 최소 힙은 부모 노드가 자식 노드보다 작거나 같은 이진 트리
# 최소힙을 이용하여 다음 연산을 지원하는 프로그램 만들기 
# 1. 배열에 자연수 x를 넣는다.
# 2. 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.


if __name__ == "__main__":
    n = int(input())
    heap = []
    for _ in range(n):
        x = int(input())
        if x == 0:
            if len(heap) == 0:
                print(0)
            else:
                print(hq.heappop(heap))
        else:
            hq.heappush(heap, x)
