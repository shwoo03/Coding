# 모든 단어의 길이는 홀수 
# 비밀번호 목록에 있는 단어들 중 거꾸로 읽어도 같은 단어가 존재하면 그 단어의 중간 글자를 출력하세요 

N = int(input())
list_word = []

for i in range(N):
    word = input()
    
    list_word.append(word)

for i in range(N):
    word = list_word[i]
    word_reverse = word[::-1]
    
    if word in list_word and word_reverse in list_word:
        print(len(word), end=" ")
        print(word[len(word)//2])
        break