while True:
    n = int(input())
    if n == -1:
        break

    list_num = []

    for i in range(2,n):
        if n % i == 0:
            list_num.append(i)
        else:
            continue
    
    sum = 1
    for i in list_num:
        sum += i
    
    if sum == n:
        print(f"{n} = 1 ",end="")
        for num in list_num:
            print(f"+ {num} ",end="")
    else:
        print(f"{n} is NOT perfect.")

