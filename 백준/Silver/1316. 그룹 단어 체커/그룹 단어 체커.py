import math
import sys
input = sys.stdin.readline


# 각 단어는 연속하지 않는 이상 한 번만 나와야 한다.
# 이런것을 그룹단어라고 하는데 그룹 단어의 수를 게산해야 함 
# 일단 중복

if __name__ == "__main__":
    T = int(input())
    count = 0

    for i in range(T):
        word = input().strip()
        is_group = True
        word_list = []
        prev_ch = ''

        for ch in word:
            if ch != prev_ch:
                if ch in word_list:
                    is_group = False
                    break

                word_list.append(ch)
            elif ch == prev_ch:
                continue
            
            prev_ch = ch
        
        if is_group:
            count += 1
        
    print(count)






