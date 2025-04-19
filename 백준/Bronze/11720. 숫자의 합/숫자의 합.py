import sys
input = sys.stdin.readline








if __name__ == "__main__":
    N = int(input())
    num = input()

    num = list(map(int, num.strip()))
    print(sum(num))