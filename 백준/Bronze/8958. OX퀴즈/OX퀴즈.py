import sys
input = sys.stdin.readline


# O는 맞고 X는 틀림
# 문제의 점수는 연속된 O의 개수만큼 됨 
# OOXXOXXOOO의 점수는 10점 
# 결과 구하는 프로그램 작성 


if __name__ == "__main__":
    # X를 기준으로 문자열 자르기 
    N = int(input())

    for i in range(N):
        string = input()
        sum_num = 1
        result = 0

        for ch in string:
            if ch == 'O':
                result += sum_num
                sum_num += 1
            else:
                sum_num = 1

        print(result)

