# 정수를 저장하는 덱(Deque) 구현
# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys 

class Deque:
    def __init__ (self):
        self.deque = []
    
    def push_front(self, X):
        self.deque.insert(0, X)
    
    def push_back(self, X):
        self.deque.append(X)
    
    def pop_front(self):
        if self.empty():
            return -1
        else:
            return self.deque.pop(0)
    
    def pop_back(self):
        if self.empty():
            return -1
        else:
            return self.deque.pop()
    
    def size(self):
        return len(self.deque)
    
    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0
    
    def front(self):
        if self.empty():
            return -1
        else:
            return self.deque[0]
    
    def back(self):
        if self.empty():
            return -1
        else:
            return self.deque[-1]

N = int(sys.stdin.readline())
deque = Deque()

for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push_front':
        deque.push_front(command[1])
    elif command[0] == 'push_back':
        deque.push_back(command[1])
    elif command[0] == 'pop_front':
        print(deque.pop_front())
    elif command[0] == 'pop_back':
        print(deque.pop_back())
    elif command[0] == 'size':
        print(deque.size())
    elif command[0] == 'empty':
        print(deque.empty())
    elif command[0] == 'front':
        print(deque.front())
    elif command[0] == 'back':
        print(deque.back())
    else:
        break