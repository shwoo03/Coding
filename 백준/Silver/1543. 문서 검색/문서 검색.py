# 영어로만 이루어진 문서를 검색하는 함수를 만들려고 한다. 
# 어떤 단어가 총 몇 번 등장하는지 세려고 한다.
# 함수는 중복되어 세는 것은 빼고 세야 한다. 

def count_words(ch, match_ch):
    ch = ch.replace(" ", "")
    match_ch = match_ch.replace(" ", "")
    
    count = 0
    i = 0
    while i <= len(ch) - len(match_ch):
        if ch[i:i+len(match_ch)] == match_ch:
            count += 1
            i += len(match_ch)  
        else:
            i += 1
    
    return count

ch = input()
match_ch = input()

result = count_words(ch, match_ch)
print(result)

