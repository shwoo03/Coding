import math
import sys
input = sys.stdin.readline



# 주어진 M을 넘지 않는 한도에서 카드 합을 최대로 만들어야 한다. 



if __name__ == "__main__":
    card_num, max_num = map(int,input().split())

    list_num = list(map(int, input().split()))
    max = 0
    
    for first_num in range(card_num-2):
        for second_num in range(first_num+1, card_num-1):
            for third_num in range(second_num+1, card_num):
                sum = list_num[first_num] + list_num[second_num] + list_num[third_num]

                if max < sum and sum <= max_num:
                    max = sum
    
    print(max)


