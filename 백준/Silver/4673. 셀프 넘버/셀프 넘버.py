# 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수 
# 예를 들어, d(75) = 75+7+5 = 87이다.

# 이것으로 무한 수열을 만들 수 있다. 
# 그렇다면 생성자 함수에서 10000 까지의 수를 빼면 된다. 

def d(n):
    result = n
    while n > 0:
        result += n % 10
        n = n // 10
    return result

numbers = set(range(1, 10001))
generated_numbers = set()

for i in range(1, 10001):
    generated_numbers.add(d(i))

self_numbers = numbers - generated_numbers

for self_number in sorted(self_numbers):
    print(self_number)