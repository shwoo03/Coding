import sys
input = sys.stdin.readline








if __name__ == "__main__":
    N = int(input())
    num_list = list(map(int,input().split()))
    print(f"{min(num_list)} {max(num_list)}")