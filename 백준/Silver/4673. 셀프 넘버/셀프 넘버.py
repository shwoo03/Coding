import math
import sys
input = sys.stdin.readline


# 셀프 넘버는 n과 n의 각 자리 수를 더하는 함수다 
# 이때 33은 39의 생성자이고 39는 51의 생성자이다. 
# 하지만 생성자가 없는 숫자를 셀프 넘버라고 하는데 셀프 넘버를 모두 출력하는 코드 작성 
# 10000 보다 작거나 같은 수 기준 


# 생성자 수를 모두 구하고 중복을 없앤다음 
# 10000 이하의 값에서 list에 없는 값 출력 


if __name__ == "__main__":
    list_self_num = set()

    for i in range(1, 10001):
        list_self_num.add(i + sum(map(int, str(i))))
    
    for i in range(1, 10001):
        if i not in list_self_num:
            print(i)


