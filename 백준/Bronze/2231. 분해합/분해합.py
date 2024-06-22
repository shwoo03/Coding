n = int(input()) 
result = 0
for candidate in range(1, n + 1):
        decomposition_sum = candidate + sum(map(int, str(candidate)))

        if decomposition_sum == n:
            result = candidate
            break

print(result)