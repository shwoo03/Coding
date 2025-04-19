import sys
input = sys.stdin.readline








if __name__ == "__main__":
    h, m = map(int,input().split())
    time = int(input())

    m += time

    h += m // 60
    m = m % 60

    if( h > 23):
        h -= 24

    print(f"{h} {m}")