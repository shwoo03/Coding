import math
import sys
input = sys.stdin.readline


# 어떤 양의 정수 x의 각 자리가 등차수열을 이룬다면 그 수를 한수라고 함 
# 한수의 개수를 출력하는 프로그램 작성 N이하의 수 

def is_hansu(x):
    num = list(map(int, str(x)))
    if len(num) <= 2:
        return True
    else:
        return (num[0] - num[1]) == (num[1] - num[2])


if __name__ == "__main__":
    N = int(input())

    # 1, 10, 100의 자리일 때로 경우를 나눠서 판단하면 됨 
    count = 0
    for i in range(1, N + 1):
        if is_hansu(i):
            count += 1

    print(count)
    
