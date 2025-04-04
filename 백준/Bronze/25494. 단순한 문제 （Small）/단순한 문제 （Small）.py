# a,b,c가 주어질 때, 다음 조건을 만족하는 정수 쌍 x,y,z의 개수를 구해라
# 1 <= x <= a
# 1 <= y <= b
# 1 <= z <= c
# x mod y = y mod z = z mod x

T = int(input())

for _ in range(T):
    a,b,c = map(int, input().split())
    count = 0

    for x in range(1, a+1):
        for y in range(1, b+1):
            for z in range(1, c+1):
                if x % y == y % z == z % x:
                    count += 1
    
    print(count)