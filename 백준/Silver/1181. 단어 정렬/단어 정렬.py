N = int(input())

list_chr = []
for i in range(N):
    list_chr.append(input())

list_chr = list(set(list_chr))  # 중복 제거
list_chr.sort(key=lambda x: (len(x), x))  # 길이 우선, 길이가 같으면 사전순으로 정렬

for ch in list_chr:
    print(ch)
