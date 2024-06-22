T = int(input())

cases = [(0,0) for _ in range(41)]
cases[0] = (1,0)
cases[1] = (0,1)
for i in range(2,41):
    cases[i] = (cases[i-1][0] + cases[i-2][0], cases[i-1][1] + cases[i-2][1])

for i in range(T):
    case = int(input())
    print(*cases[case])