import sys
input = sys.stdin.readline



# 모든 방은 수직으로 먼저 채워진다.
# 1층 1호부터 N호까지 채워지고
# 그 다음 2층 1호부터 N호까지 채워진다.
# 따라서 N번째 손님은 N%H 층의 N//H 호에 배정된다.


if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        H, W, N = map(int, input().split())

        if N % H == 0:
            floor = H
            room = N // H
        else:
            floor = N % H
            room = N // H + 1

        print(f"{floor}{room:02d}")

