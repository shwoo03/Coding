import sys
input = sys.stdin.readline

bitset = 0

for _ in range(int(input())):
    command = input().split()
    
    if command[0] == 'add':
        x = int(command[1])
        bitset |= (1 << x)
    elif command[0] == 'remove':
        x = int(command[1])
        bitset &= ~(1 << x)
    elif command[0] == 'check':
        x = int(command[1])
        print(1 if bitset & (1 << x) else 0)
    elif command[0] == 'toggle':
        x = int(command[1])
        bitset ^= (1 << x)
    elif command[0] == 'all':
        bitset = (1 << 21) - 1
    elif command[0] == 'empty':
        bitset = 0
