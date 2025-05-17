import math
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline


# M미터의 나무가 필요함 
# H미터 지정하여 나무를 자르면 잘린 나무를 가져감 
# 단, 나무를 필요한 만큼만 가져가려고 함 
# 절단기에 설정할 수 있는 높이의 최대값을 구하시오 
# 최대/최소 나무 길이를 가진 요소의 중간부터 탐색을 진행하면 됨 
def binary_search(list_tree, start, end, target, tree_num):
    max_tree_high = 0

    while start <= end:
        mid = (start + end) // 2
        tree_sum = 0
        for tree in list_tree:
            if (tree - mid) <= 0:
                tree_sum += 0
            else:
                tree_sum += tree - mid
        

        if tree_sum == target:
            return mid
        elif tree_sum < target:
            end = mid - 1
        else:
            start = mid + 1
            if max_tree_high < mid:
                max_tree_high = mid
    
    return max_tree_high




if __name__ == "__main__":
    tree_num, tree_length = map(int,input().split())
    list_tree = list(map(int, input().split()))
    list_tree.sort()
    result = -1
    
    print(binary_search(list_tree, 0, list_tree[-1], tree_length, tree_num))







