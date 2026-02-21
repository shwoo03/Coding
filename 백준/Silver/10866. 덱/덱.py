from collections import deque

dq = deque()

N = int(input())

for _ in range(N):
    commands = input().split()

    if commands[0] == 'push_front':
        dq.appendleft(commands[1])
    elif commands[0] == 'push_back':
        dq.append(commands[1])
    elif commands[0] == 'pop_front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif commands[0] == 'pop_back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())
    elif commands[0] == 'size':
        print(len(dq))
    elif commands[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif commands[0] == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif commands[0] == 'back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])