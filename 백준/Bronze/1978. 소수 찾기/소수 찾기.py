n = int(input())
list_num = list(map(int,input().split()))
prime_num = 0

for i in list_num:
    if i <= 1:  # 1보다 작은 수는 소수가 아님
        continue
    result = True        # 0 이면 소수 1이면 소수가 아니다 
    
    for j in range(2,i,1):
        if i % j == 0:
            result = False
        else:
            pass
    
    if result == False:
        pass
    else:
        prime_num += 1

print(prime_num)

