# 정수를 저장하는 큐를 만든 다음, 입력으로 주어지는 명령을 처리하는 프로그램 작성 
# push X: 정수 X를 큐에 넣는 연산
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력, 없는 경우 -1 출력
# size: 큐에 들어있는 정수의 개수 출력
# empty: 큐가 비어있으면 1, 아니면 0 출력
# front: 큐의 가장 앞에 있는 정수 출력, 없는 경우 -1 출력
# back: 큐의 가장 뒤에 있는 정수 출력, 없는 경우 -1 출력

import sys 
input = sys.stdin.readline

n = int(input())
queue = []
front_index = 0  # front index 기준을 직접 수정하는 방식 사용 

for _ in range(n):
    command = input().split()
    
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':   # pop는 시간 복잡도 O(n)이므로 front_index를 사용하여 시간 복잡도를 줄임
        if front_index < len(queue):
            print(queue[front_index])  
            front_index += 1 
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(queue) - front_index)
    elif command[0] == 'empty':
        if front_index >= len(queue):
            print(1)  
        else:
            print(0) 
    elif command[0] == 'front':
        if front_index < len(queue):
            print(queue[front_index])  # 큐의 앞쪽 요소 출력
        else:
            print(-1)
    elif command[0] == 'back':
        if front_index < len(queue):
            print(queue[-1])  
        else:
            print(-1)