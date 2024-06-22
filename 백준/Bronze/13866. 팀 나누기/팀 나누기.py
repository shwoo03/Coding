list_skill = list(map(int,input().split()))

list_skill.sort()
result = (list_skill[0]+list_skill[3]) - (list_skill[1]+list_skill[2])
print(abs(result))