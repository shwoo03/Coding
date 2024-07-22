# y 좌표가 증가하는 순으로, 같으면 x 좌표가 증가하는 순으로 정렬한 다음 출력 

N = int(input())

arr = []
for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort(key=lambda x: (x[1], x[0]))

for x, y in arr:
    print(x, y)