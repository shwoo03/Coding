import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# 나무 M미터가 필요함 목재는 다음과 같이 절단함 
# 절단기에 H높이를 지정, 한 줄에 연속해있는 나무를 모두 절단 
# H보다 낮은 나무는 절단되지 않음
# 즉, 20,15,10,17이면 H=15일때 20-15+15-10+17-15=7
# 필요한 만큼만 가져갈거임, 최대 높이를 구하는 문제


# 탐색 해야함 
def binary_search(trees, target_height, tree_num):
    trees.sort(reverse=True) # 나무를 내림차순으로 정렬
    left = 0
    right = max(trees) # 나무의 최대 높이
    answer = 0

    while left <= right:
        mid = (left + right) // 2 # 중간값
        total = 0 # 나무의 총 길이

        for tree in trees:
            if tree > mid: # 나무가 mid보다 크면 잘림
                total += tree - mid # 잘린 나무의 길이 더함

        if total >= target_height: # 잘린 나무의 길이가 목표 높이 이상이면
            answer = mid # 현재 높이를 정답으로 저장
            left = mid + 1 # 높이를 올림
        else:
            right = mid - 1 # 높이를 내림

    return answer



if __name__ == "__main__":
    tree_num, target_height = map(int, input().split()) # 나무의 개수, 필요한 나무의 길이
    trees = list(map(int, input().split())) 
    

    print(binary_search(trees, target_height, tree_num))



