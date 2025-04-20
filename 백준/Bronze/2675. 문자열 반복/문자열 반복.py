import sys
input = sys.stdin.readline





if __name__ == "__main__":
    T = int(input())

    for i in range(T):
        n, string = input().split()
        n = int(n)
        

        for ch in string:
            print(ch * n, end="")

        print()

