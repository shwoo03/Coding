from itertools import combinations

list_num = []

for i in range(9):
    list_num.append(int(input()))

list_num.sort()

for comb in combinations(list_num, 7):
    if sum(comb) == 100:
        for num in comb:
            print(num)
        break