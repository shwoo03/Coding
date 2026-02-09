# N -> 카드 개수 
# list_num -> 카드에 적혀있는 정수 
# M -> 질문 개수?
# list_m -> 질문에 적힌 정수

N = int(input())
list_num = list(map(int, input().split()))
M = int(input())
list_m = list(map(int, input().split()))

dict_m = {
    num: 0 for num in list_m
}

for num in list_num:
    if num in dict_m:
        dict_m[num] += 1

for result in dict_m.values():
    print(result, end=' ')