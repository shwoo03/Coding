# 1부터 N까지의 수를 이어서 쓰면 다음과 같이 새로운 하나의 수를 얻을 수 있다.
# 1234567891011121314151617181920212223...
# 이렇게 만들어진 새로운 수는 몇 자리 수일까? 이 수의 자릿수를 구하는 프로그램을 작성하시오.

N = int(input())
jarisu = 0
current = 1  # 현재 자릿수의 시작 숫자
digits = 1   # 현재 자릿수 (1자리, 2자리, 3자리 등)

while current <= N:
    next_number = current * 10  # 다음 자릿수의 시작 숫자 (10, 100, 1000, ...)
    
    # 현재 자릿수 범위에서 N까지의 숫자 개수
    count = min(N - current + 1, next_number - current)
    
    # 해당 범위의 숫자들의 전체 자릿수를 누적합
    jarisu += count * digits
    
    # 다음 자릿수로 이동
    digits += 1
    current = next_number

print(jarisu)
