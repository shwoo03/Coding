# P[0], P[1], P[N-1]은 0 부터 N-1 까지의 수를 한 번씩 포함하는 수열이다.
# 수열 P를 길이가 N인 배열 A에 적용하면 길이가 N인 배열 B가 된다.
# 적용하는 방법은 B[P[i]] = A[i] 이다.

# 배열 A가 주어지고, 배열 B가 주어지면, P를 적용한 결과가 비내림차순이 되는 수열을 찾는 프로그램 작성 
# 비내림차순이란, 각각의 원소가 바로 앞에 있는 원소보다 크거나 같은 경우를 말한다.
# 만약 그러한 수열이 여러 개라면, 사전순으로 가장 앞서는 것을 출력한다.

N = int(input())
A = list(map(int, input().split()))

sorted_indices = sorted(range(N), key=lambda i: A[i])

P = [0] * N
B = [0] * N

# 오름차순 정렬 후 idx 기록하고 원래 인덱스에 맞게 P에 기록하면 됨 
for idx, original_index in enumerate(sorted_indices):
    P[original_index] = idx
    B[idx] = A[original_index]

print(' '.join(map(str, P)))  