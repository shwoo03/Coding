import sys
input = sys.stdin.readline








if __name__ == "__main__":
    a, b, c = map(int, input().split())

    if a == b == c:
        reward = 10000 + a * 1000
    elif a == b or a == c:
        reward = 1000 + a * 100
    elif b == c:
        reward = 1000 + b * 100
    else:
        reward = max(a, b, c) * 100

    print(reward)