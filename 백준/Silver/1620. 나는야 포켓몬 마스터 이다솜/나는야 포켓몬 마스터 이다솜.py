# 첫 줄에 도감에 있는 포켓몬의 개수  N과 맞춰야 하는 문제의 개수 M이 주어진다.
# 둘째 줄부터 N개의 줄에 포켓몬의 번호가 1번인 포켓몬부터 N번인 포켓몬까지의 이름이 주어진다.
# 포켓몬의 이름은 모두 영어이고, 첫 글자만 대문자이고, 나머지 문자는 소문자이다.
# 일부 포켓몬은 마지막 문자만 대문자일 수도 있다.
# 그 다음 줄부터 M개의 줄에 내가 맞춰야하는 문제가 입력으로 들어온다.
# 문제가 알파벳으로 들어오면, 해당 알파벳으로 시작하는 포켓몬의 번호를 출력한다.
# 숫자로 들어오면, 그 번호에 해당하는 포켓몬의 이름을 출력한다.

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pokemon_num_to_name = {}
pokemon_name_to_num = {}

for i in range(1, N + 1):
    name = input().strip()
    pokemon_num_to_name[i] = name
    pokemon_name_to_num[name] = i

for _ in range(M):
    question = input().strip()
    if question.isdigit(): 
        print(pokemon_num_to_name[int(question)])
    else: 
        print(pokemon_name_to_num[question])