while(True):
    ls_n = list(map(int,input().split()))
    ls_n.sort()

    if sum(ls_n) == 0:
        break

    if ls_n[2] >= ls_n[0] + ls_n[1]:
        print("Invalid")
    elif ls_n[0] == ls_n[1] and ls_n[1] == ls_n[2] and ls_n[2] == ls_n[0]:
        print("Equilateral")
    elif ls_n[0] == ls_n[1] or ls_n[1] == ls_n[2] or ls_n[2] == ls_n[0]:
        print("Isosceles")
    elif ls_n[0] != ls_n[1] and ls_n[1] != ls_n[2] and ls_n[2] != ls_n[0]:
        print("Scalene")
