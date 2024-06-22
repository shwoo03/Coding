ch = input().lower()

list_count = [0 for i in range(26)]

for c in ch:
    if 'a' <= c <= 'z':  # 알파벳인 경우에만 처리
        list_count[ord(c) - ord('a')] += 1

max_count = max(list_count)

if list_count.count(max_count) > 1:
    print("?")
else:
    max_index = list_count.index(max_count)
    print(chr(max_index + ord('a')).upper())