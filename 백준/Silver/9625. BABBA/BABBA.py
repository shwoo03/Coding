# 화면에 A만 표시되어 있고, 버튼을 누르니 글자가 B로 변함 
# 즉 화면의 모든 B는 BA로 바뀌고, A는 B로 바뀐다는 것을 알게되었다.
# 버튼을 K번 눌렀을 때, 화면에 A의 B의 개수는 몇 개가 될까? 

def fibonacci_count(k):
    if k == 1:
        return 0, 1
    a_count, b_count = 0, 1
    for i in range(2, k+1):
        new_a_count = b_count
        new_b_count = a_count + b_count
        a_count = new_a_count
        b_count = new_b_count
    return a_count, b_count

# 입력 및 결과 출력
K = int(input())
a_count, b_count = fibonacci_count(K)
print(a_count, b_count)
