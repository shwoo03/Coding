import math
import sys
input = sys.stdin.readline



if __name__ == "__main__":
    T = int(input())
    list_num = []

    for i in range(T):
        list_num.append(int(input()))
    
    list_num.sort()
    for n in list_num:
        print(n)







