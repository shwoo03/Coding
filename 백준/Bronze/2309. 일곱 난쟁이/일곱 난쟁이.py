import math
import sys
input = sys.stdin.readline


# 일곱 난쟁이의 키의 합은 100인데 간첩 2명 존재 
# 일곱 난쟁이를 찾아서 오름차순으로 출력하기 


if __name__ == "__main__":
    list_nan = []
    for i in range(9):
        list_nan.append(int(input()))
    
    # 음.... 7중 포문을 사용할 수는 없으니까 
    # total_sum - 2명 키 조합 이 100이 되는 것을 찾아서 출력해야 할듯 
    total_sum = sum(list_nan)
    remove_value1 = 0
    remove_value2 = 0

    for i in range(9):
        for j in range(i+1, 9):
            if (total_sum - (list_nan[i] + list_nan[j])) == 100:
                remove_value1 = list_nan[i]
                remove_value2 = list_nan[j]
    
    list_nan.remove(remove_value1)
    list_nan.remove(remove_value2)

    
    list_nan.sort()
    for n in list_nan:
        print(n)

    
