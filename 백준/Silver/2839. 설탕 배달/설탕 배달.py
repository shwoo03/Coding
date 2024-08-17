# 상근이는 설탕 N KG 배달해야함 
# 설탕은 3KG 또는 5KG 봉지에 담겨져 있음
# 최대한 적은 봉지를 들고 가려고 함
# N KG를 배달하기 위해 가져가야 하는 봉지의 최소 개수를 출력
# 만들 수 없다면 -1 출력 

N = int(input())

result = 0
while True:
    if N % 5 == 0:
        result += N // 5
        break
    
    N -= 3
    result += 1

print(-1) if N < 0 else print(result)