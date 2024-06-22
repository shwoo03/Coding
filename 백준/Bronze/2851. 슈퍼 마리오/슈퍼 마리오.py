sum = 0

for i in range(10):
    n = int(input())
    sum += n
    if sum > 100:
        if sum - 100 > 100 - (sum - n):
            sum -= n
            break
        else:
            break

print(sum)