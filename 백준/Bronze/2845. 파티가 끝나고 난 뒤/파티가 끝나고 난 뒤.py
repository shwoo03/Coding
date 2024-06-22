n,a = map(int,input().split())

list_num = list(map(int,input().split()))

for i in list_num:
    print(i-(n*a),end=" ")