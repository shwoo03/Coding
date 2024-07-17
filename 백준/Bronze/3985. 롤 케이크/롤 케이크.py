# L 미터 롤 케잌을 N명에게 나누어 준다. 
# 방청객은 종이에 자신이 원하는 조각을 적어 제출한다. P 에서 K 만큼 
# 가장 많은 케이크 조각을 받을 것으로 기대한 방청객의 번호와 실제로 가장 많은 케이크 조각을 받는 방청객의 번호를 구하는 프로그램을 작성

L = int(input())
N = int(input())

dict_num = {i: None for i in range(1, L + 1)}
expect = [0,0]
real = [0 for i in range(N)]

for i in range(N):
    P, K = map(int, input().split())
    if expect[1] < K - P: 
        expect[1] = K - P
        expect[0] = i + 1
    
    for key in range(P, K + 1):

        if dict_num[key] == None:
            dict_num[key] = i + 1
            real[i] += 1
    

print(expect[0])
print(real.index(max(real)) +1 ) 


