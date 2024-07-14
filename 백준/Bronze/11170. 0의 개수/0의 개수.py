T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    result = 0
    
    for string in range(N, M+1):
        result += str(string).count('0')
    
    print(result)

