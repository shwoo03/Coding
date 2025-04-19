import sys
input = sys.stdin.readline








if __name__ == "__main__":
    N = int(input())

    for i in range(N):
        a,b = map(int,input().split())
        print(a+b)