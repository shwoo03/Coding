import sys
input = sys.stdin.readline


# stack에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자.
# 임의 수열이 주어지면 스택을 이용하여 그 수열을 만들 수 있는지 없는지 있다면 
# 어떤 순서로 push pop을 해야하는지 출력




if __name__ == '__main__':
    n = int(input())
    stack = []
    input_list = []
    result = []
    idx = 0

    for i in range(n):
        input_list.append(int(input()))
        stack.append(i + 1)
        result.append("+")

        while stack and stack[-1] == input_list[idx]:
            pop_num = stack.pop()
            result.append("-")
            idx += 1
            if idx == n:
                break


    if len(stack) != 0:
        print("NO")
    else:
        for i in result:
            print(i)
