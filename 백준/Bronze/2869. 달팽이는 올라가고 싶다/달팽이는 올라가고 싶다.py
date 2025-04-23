import math
import sys
input = sys.stdin.readline



# V 미터 나무를 올라가는데 낮에는 A미터 올라감 
# 자는 동안 B만큼 미끄러짐 
# 며칠이 걸리나 


if __name__ == "__main__":
    up, down, v = map(int,input().split())
    result = 0
    day_up = up - down
    half_day_up = up

    total_day = math.ceil((v - down) / day_up)
    print(int(total_day))
