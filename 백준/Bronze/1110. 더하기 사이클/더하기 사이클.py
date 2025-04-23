import math
import sys
input = sys.stdin.readline



# 0 <= x <= 99 일때 10 보다 작으면 0 붙이고 각 자리 수를 더함 
# 주어진 수의 오른쪽과 계산 값의 오른쪽 수를 이어 붙여서 새로운 수 만들기 
# 26 -> 2 + 6 = 8
# 68 -> 6 + 8 = 14
# 84 



if __name__ == "__main__":
    num = input().strip()
    
    # 1자리 수일 경우 0붙이기
    if len(num) == 1:
        num = '0' + num
    
    original_num = num
    count = 0

    while True:
        # 각 자리수 더하기
        sum_digits = int(num[0]) + int(num[1])
        # 새로운 숫자 만들기
        num = num[1] + str(sum_digits % 10)
        count += 1
        
        if num == original_num:
            break

    print(count)

