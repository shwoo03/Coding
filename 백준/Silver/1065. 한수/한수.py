# 정수 X의 각 자리가 등차수열을 이루면, 그 수를 한수라고 한다. 
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
# N이 주어지고, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

N = int(input())

def hansu(N):
    count = 0
    for i in range(1, N+1):
        if i < 100:
            count += 1
        else:
            num = list(map(int, str(i)))
            if num[0] - num[1] == num[1] - num[2]:
                count += 1
    return count

print(hansu(N))