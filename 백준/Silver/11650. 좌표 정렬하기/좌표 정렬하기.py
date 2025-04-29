import math
import sys
input = sys.stdin.readline


# x,y 좌표 정렬하기 
# 1. x좌표 증가하는 순으로 하고 
# 2. 같으면 y좌표 증가하는 순으로 



if __name__ == "__main__":
    T = int(input())
    list_coordinate = []

    for i in range(T):
        x, y = map(int,input().split())
        list_coordinate.append([x,y])
    
    orderd_list = sorted(list_coordinate, key=lambda coordinate: (coordinate[0], coordinate[1]))
    
    for coordinate in orderd_list:
        print(coordinate[0], coordinate[1])