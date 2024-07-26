# Rick Astley의 공약 리스트
rick_astley_promises = [
    "Never gonna give you up",
    "Never gonna let you down",
    "Never gonna run around and desert you",
    "Never gonna make you cry",
    "Never gonna say goodbye",
    "Never gonna tell a lie and hurt you",
    "Never gonna stop"
]

N = int(input())
input_promises = [input().strip() for _ in range(N)]

for promise in input_promises:
    if promise not in rick_astley_promises:
        print("Yes")
        break
else:
    print("No")
