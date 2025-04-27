import math
import sys
input = sys.stdin.readline


# 단어가 주어지면 몇 개의 크로아티아 알파멧으로 이루어져 있는지 출력한다.
# 목록에 존재하지 않는 알파벳은 한 글자씩 센다 


if __name__ == "__main__":
    word = input().strip()
    c_alpha_list = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
    result = 0
    index = 0

    while index < len(word):
        if word[index:index+3] == "dz=":
            result += 1
            index += 3
        elif word[index:index+2] in c_alpha_list:
            result += 1
            index += 2
        else:
            result += 1
            index += 1

    print(result)