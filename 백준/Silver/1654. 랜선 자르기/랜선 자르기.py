import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# N개의 랜선을 만들어야 하는데 
# 이미 K개의 랜선이 있음 하지만 길이는 다 다름 
# N개의 같은 길이의 랜선으로 만들고 싶어서 K개를 잘라서 만들어야 함 
# 랜선은 항상 정수 길이로 자르고 그 과정에서 손실은 없음 
# N개보다 많이 만들어도 됨, 이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오 

# 이분 탐색 
def binary_search(lans, N):
    start = 1
    end = max(lans)
    result = 0

    while start <= end:
        mid = (start + end) // 2
        count = 0

        for lan in lans:
            count += lan // mid

        if count >= N:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return result


if __name__ == "__main__":
    K, N = map(int, input().split())
    lans = []
    
    for _ in range(K):
        lans.append(int(input()))
    
    result = binary_search(lans, N)
    print(result)

