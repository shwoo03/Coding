import sys
input = sys.stdin.readline

N, M = map(int, input().split())

list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))


result = list_A + list_B
result.sort()

print(' '.join(map(str, result)))
