import sys
input = sys.stdin.readline


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result






if __name__ == "__main__":
    N = int(input())
    print(factorial(N))