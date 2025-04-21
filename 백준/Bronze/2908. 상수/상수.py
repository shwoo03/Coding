import sys
input = sys.stdin.readline



# 수를 거꾸로 읽어서 수를 비교하는 프로그램 작성 


if __name__ == "__main__":
    x, y = map(str, input().split())

    x = x[::-1]
    y = y[::-1]

    if(int(x) > int(y)):
        print(int(x))
    else:
        print(int(y))

