import math
import sys
input = sys.stdin.readline


# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 
# 1. 길이가 짧은 것부터 
# 2. 길이가 같으면 사전 순으로 정렬 
# 3. 중복 단어는 하나만 남기고 제거 



if __name__ == "__main__":
    T = int(input())
    list_words = []

    for i in range(T):
        list_words.append(input().strip())

    
    list_words = list(set(list_words))
    list_words = sorted(list_words, key=lambda x: (len(x), x))
    
    for ch in list_words:
        print(ch)
