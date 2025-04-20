import sys
input = sys.stdin.readline






if __name__ == "__main__":
    x,y,w,h = map(int, input().split())

    result = min(w-x, x, y, h-y)
    print(result)
