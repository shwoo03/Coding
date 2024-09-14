# 길이가 N으로 같은 문자열 X와 Y가 있을 때, 두 문자열 X와 Y의 차이는 X[i] ≠ Y[i]인 i의 개수이다. 
# 예를 들어, X=”jimin”, Y=”minji”이면, 둘의 차이는 4이다.

# 두 문자열 A와 B가 주어진다. 이때, A의 길이는 B의 길이보다 작거나 같다. 
# 이제 A의 길이가 B의 길이와 같아질 때 까지 다음과 같은 연산을 할 수 있다.

# A의 앞에 아무 알파벳이나 추가한다.
# A의 뒤에 아무 알파벳이나 추가한다.
# 이때, A와 B의 길이가 같으면서, A와 B의 차이를 최소로 하는 프로그램을 작성하시오.

a, b = input().split()
a_len = len(a)
b_len = len(b)

a = a.strip()
b = b.strip()

min_diff = 51

# 길이가 같으면 그냥 다른 문자 개수만 세면 된다.
if a_len == b_len:
    cnt = 0
    for i in range(a_len):
        if a[i] != b[i]:
            cnt += 1
    print(cnt)
else:
    # 길이가 다르면 길이가 같아질 때까지 앞이나 뒤에 문자를 추가해야 한다.
    # 그런데 아무 알파벳이나 추가할 수 있으므로, 길이가 같아지기 위해 추가해야 하는 문자의 개수는 
    # 가장 최소한의 차이가 나는 문자열을 찾으면 나머지는 아무 문자나 추가해도 되니깐 차이가 발생하지 않음 
    # 예를 들어서 abc , topabcoder이고 abc가 중간에 포함되어 있기 대문에 차이는 0이다. -> 아무 문자나 추가해도 되니깐 
    # 따라서 문자열을 한개씩 옮기면서 부분 문자열과 전체 문자열의 차이가 최소인 것을 찾으면 된다. 
    for i in range(b_len - a_len + 1):
        cnt = 0
        for j in range(a_len):
            if a[j] != b[i + j]:
                cnt += 1
        if min_diff > cnt:
            min_diff = cnt
    
    print(min_diff)

