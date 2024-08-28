# 어느 날, 양수 N을 봤는데, 미르코는 30을 존경하기 때문에, 찾은 수에 포함된 숫자들을 섞어 30의 배수가 되는 가장 큰 수를 만들고 싶어한다.

N = input()

digits = list(N)

# 30의 배수는 3의 배수이면서 10의 배수이다.
# 즉, 0이 하나라도 없으면 30의 배수가 될 수 없다.
if '0' not in digits:
    print(-1)
else:
    # 또한 각 자리수의 합이 3의 배수이어야 한다.
    digit_sum = sum(map(int, digits))
    if digit_sum % 3 != 0:
        print(-1)
    else:
        # 조건을 만족하면 내림차순으로 가장 큰 수를 만들어서 출력 
        digits.sort(reverse=True)
        print(''.join(digits))
