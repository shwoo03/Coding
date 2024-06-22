T = int(input())

for _ in range(T):
    num_school = int(input())
    dict_school = {
        }
    
    for _ in range(num_school):
        school_name, school_score = input().split()
        dict_school[school_name] = int(school_score)
    
    max_school = max(dict_school, key=dict_school.get)
    print(max_school)