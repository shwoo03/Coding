# 스네이크 버드는 뱀과 새의 모습을 닮은 생물체이다. 
# 주요 먹이는 과일이고 과일 하나를 먹으면 길이가 1만큼 늘어난다. 
# 과일은 지상으로부터 일정 높이를 두고 떨어져 있으며 i 번째 과일의 높이는 height[i]이다.
# 자신의 길이보다 작거나 같은 높이에 있는 과일들을 먹을 수 있다. 
# 처음 길이가 L 일 때 먹어 늘릴 수 있는 최대 길이를 구하시오.

N , L = map(int, input().split())

for i in range(N):
    height = list(map(int, input().split()))
    height.sort()
    
    for j in range(len(height)):
        if height[j] <= L:
            L += 1
        else:
            print(L)
            exit()  
        
        if j == len(height)-1:
            print(L)
            exit()