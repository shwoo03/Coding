N = int(input())
list_kg_cm = []

for i in range(N):
    temp = list(map(int, input().split()))
    temp.append(1)
    list_kg_cm.append(temp)
    # [[55, 185, 0], ...] 형태 반환 

for i in range(N):
    for j in range(i+1, N):
        if (list_kg_cm[i][0] > list_kg_cm[j][0]) and (list_kg_cm[i][1] > list_kg_cm[j][1]):
            list_kg_cm[j][2] += 1
        elif (list_kg_cm[j][0] > list_kg_cm[i][0]) and (list_kg_cm[j][1] > list_kg_cm[i][1]):
            list_kg_cm[i][2] += 1

for i in range(N):
    print(list_kg_cm[i][2], end=" ")
