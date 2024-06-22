import sys

n = int(sys.stdin.readline()) # 멀티탭 개수 
result = 0

for i in range(n):
    temp = int(sys.stdin.readline())
    result += temp - 1

print(result + 1)