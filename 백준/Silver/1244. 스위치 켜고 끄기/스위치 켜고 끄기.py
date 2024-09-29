# 1부터 연속적으로 번호가 붙어있는 스위치들이 있다. 스위치는 켜져 있거나 꺼져있는 상태이다. <그림 1>에 스위치 8개의 상태가 표시되어 있다. 
# ‘1’은 스위치가 켜져 있음을, ‘0’은 꺼져 있음을 나타낸다. 그리고 학생 몇 명을 뽑아서, 학생들에게 1 이상이고 스위치 개수 이하인 자연수를 하나씩 나누어주었다. 
# 학생들은 자신의 성별과 받은 수에 따라 아래와 같은 방식으로 스위치를 조작하게 된다.
# 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다. 
# 즉, 스위치가 켜져 있으면 끄고, 꺼져 있으면 켠다. <그림 1>과 같은 상태에서 남학생이 3을 받았다면, 이 학생은 <그림 2>와 같이 3번, 6번 스위치의 상태를 바꾼다.
# 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 
# 그 구간에 속한 스위치의 상태를 모두 바꾼다. 이때 구간에 속한 스위치 개수는 항상 홀수가 된다.

N = int(input())
list_switch = list(map(int, input().split()))
student = int(input())

for i in range(student):
    # 남학생은 1, 여학생은 2 
    gender, num = map(int, input().split())

    if gender == 1:
        for j in range(num-1, N, num):
            list_switch[j] = 1 - list_switch[j]
    else:
        num -= 1
        start_index = num
        end_index = num

        while start_index > 0 and end_index < N-1:
            if list_switch[start_index-1] != list_switch[end_index+1]:
                break

            start_index -= 1
            end_index += 1
        
        for j in range(start_index, end_index+1):
            list_switch[j] = 1 - list_switch[j]

for i in range(N):
    print(list_switch[i], end=" ")
    if (i + 1) % 20 == 0:
        print()