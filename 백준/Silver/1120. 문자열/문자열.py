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

if a_len == b_len:
    cnt = 0
    for i in range(a_len):
        if a[i] != b[i]:
            cnt += 1
    print(cnt)
else:
    for i in range(b_len - a_len + 1):
        cnt = 0
        for j in range(a_len):
            if a[j] != b[i + j]:
                cnt += 1
        if min_diff > cnt:
            min_diff = cnt
    
    print(min_diff)

