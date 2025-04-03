# 계단은 한 번에 한 계단씩 또는 두 계산씩 오를 수 있다.
# 단 연속 3개를 모두 밟으면 안된다.
# 마지막 계단은 무조건 밟아야 한다.
# 점수는 계단의 점수 합계이다.
# 최대 점수를 구해라 

# 해당 문제는 DP 문제이다.
# 즉 각 계단에 도달하기 전에 최대 점수를 수해놓고 더하면 된다.
# 점화식은 다음과 같음 
# dp[i] = max[dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i]]

# dp[0] = score[0]
# dp[1] = score[0] + score[1]
# dp[2] = max[score[0] + score[2], score[1] + score[2]]
# dp[3] = max[dp[1] + score[3], dp[0] + score[2] + score[3]]
# dp[4] = max[dp[2] + score[4], dp[1] + score[3] + score[4]]
# ... 이런식으로 증가하면서 최대 값을 계산하면 됨 

n = int(input())
score = [0] * n

for i in range(n):
    score[i] = int(input())

    if i == 0:
        dp = [score[0]]
    elif i == 1:
        dp.append(score[0] + score[1])
    elif i == 2:
        dp.append(max(score[0] + score[2], score[1] + score[2]))
    else:
        dp.append(max(dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i]))

print(dp[n-1])