# N 명의 학생의 이름, 국어, 영어, 수학 점수가 주어질때 
# 1. 국어 점수가 감소하는 순서
# 2. 국어 점수가 같으면 영어 점수가 증가하는 순서
# 3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서
# 4. 모든 점수가 같으면 이름이 사전순으로 증가하는 순서로 정렬 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)

N = int(input())
students = []

for _ in range(N):
    name, kor, eng, math = input().split()
    students.append((name, int(kor), int(eng), int(math)))

students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for s in students:
    print(s[0])

