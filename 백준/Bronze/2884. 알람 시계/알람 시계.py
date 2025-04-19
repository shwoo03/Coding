import sys
input = sys.stdin.readline








if __name__ == "__main__":
    h, m = map(int,input().split())

    total_time = (h * 60) + m
    total_time -= 45

    h = total_time // 60
    m = total_time % 60

    if(h < 0):
        h = 24 + h

    print(f"{h} {m}")