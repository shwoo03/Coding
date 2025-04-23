import math
import sys
input = sys.stdin.readline



# 대소문자 알파벳이 주어지면 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램 작성 

# 1. 모두 대문자로 바꾸기 
# 2. 배열로 알파벳 개수 리스트 만들기 
# 3. for로 모두 돌고 max() 함수로 출력 


if __name__ == "__main__":
    string = input().strip()
    string = string.lower()
    list_alpha = [0] * 26

    for ch in string:
        index = ord(ch) - ord('a')
        list_alpha[index] += 1
    
    if list_alpha.count(max(list_alpha)) != 1:
        print("?")
    else:
        max_alpha_index = list_alpha.index(max(list_alpha))
        print(chr(max_alpha_index + ord('A')))




