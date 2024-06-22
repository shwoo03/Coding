n,k = map(int,input().split()) # 응시자 수와 상을 받는 사람의 수 
list_score = list(map(int,input().split()))
list_score.sort()

print(list_score[len(list_score) - k])
