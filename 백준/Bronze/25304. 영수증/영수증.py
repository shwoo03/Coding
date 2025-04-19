import sys
input = sys.stdin.readline








if __name__ == "__main__":
    total = int(input())
    N = int(input())

    c_num = 0
    for i in range(N):
        money, q = map(int,input().split())
        c_num += (money * q)
    
    if(c_num == total):
        print("Yes")
    else:
        print("No")

