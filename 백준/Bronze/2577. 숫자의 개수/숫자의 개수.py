a = int(input())
b = int(input())
c = int(input())
mul = a*b*c

list_num = [0 for i in range(10)]

for num in str(mul):
    num = int(num)
    list_num[num%10] += 1

for i in list_num:
    print(i)