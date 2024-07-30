# 자유 출퇴근이고, 9~6 에 반드시 회사에 없어도 됨 
# 로그가 주어졌을 때, 현재 회사에 있는 사람을 모두 구하세요 
# 첫 줄에 로그의 수 n 이 주어지고, 다음 줄에 출입 기록이 순서대로 주어짐 
# 각 사람의 이름과 enter, leave 가 주어짐
# 회사에는 동명이인이 없고, 대소문자가 다르면 다른 이름이다. 

n = int(input())

# 현재 회사에 있으면 1 없으면 0 이라고할 것이다. 
current_people = set()

for i in range(n):
    name, action = input().split()
    
    if action == 'enter':
        current_people.add(name)
    else:
        current_people.discard(name)

for person in sorted(current_people, reverse=True):
    print(person)