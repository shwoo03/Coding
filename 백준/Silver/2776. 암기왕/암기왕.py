# 하루 동안 본 모든 정수를 수첩 1에 적음 
# X라는 정수를 오늘 본 적이 있는가를 질문했고, 봤다고 주장하는 수 들을 수첩 2에 적음 
# 수첩 2에 적혀있는 순서대로, 각각의 수에 대하여 수첩 1에 있으면 1, 없으면 0을 출력하는 프로그램을 작성하시오

T = int(input())

for _ in range(T):
    N = int(input())
    note1 = set(map(int, input().split())) 
    M = int(input())
    note2 = list(map(int, input().split()))

    for i in note2:
        if i in note1:
            print(1)
        else:
            print(0)