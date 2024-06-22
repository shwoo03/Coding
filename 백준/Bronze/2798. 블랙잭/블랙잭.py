#최대 합은 21 
# 각 카드는 양의 정수 
# n 장의 카드를 모두 숫자가 보이도록 바닥에 놓고 숫자 M을 크게 외침
# 플레이어는 시간안에 n장의 카드 중 3장을 골라야 함 
# 단 합은 M을 넘지 않고 최대한 M에 가깝게 만든다. 

n,m = map(int,input().split())
list_num = list(map(int,input().split()))
result = 0

for first in range(0,n-2,1):
    temp = 0
    for second in range(first+1,n-1,1):
        for third in range(second+1,n,1):
            temp = list_num[first] + list_num[second] + list_num[third]
            if m - result > m - temp and temp <= m:
                result = temp

print(result)