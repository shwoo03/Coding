# 어떤 반에 있는 학생들의 생일이 주어졌을 때, 가장 나이가 적은 사람과 가장 많은 사람을 구하는 포르그램을 작성 
# 각 줄에는 이름 dd mm yyyy 형식으로 주어진다. 

n = int(input())
youngest = oldest = None

for i in range(n):
    name, day, month, year = input().split()
    day = int(day)
    month = int(month)
    year = int(year)
    if oldest is None:
        oldest = (name, day, month, year)
    else:
        if (year > oldest[3]) or (year == oldest[3] and month > oldest[2]) or (year == oldest[3] and month == oldest[2] and day > oldest[1]):
            oldest = (name, day, month, year)
    
    if youngest is None:
        youngest = (name, day, month, year)
    else:
        if (year < youngest[3]) or (year == youngest[3] and month < youngest[2]) or (year == youngest[3] and month == youngest[2] and day < youngest[1]):
            youngest = (name, day, month, year)

print(oldest[0])
print(youngest[0])
