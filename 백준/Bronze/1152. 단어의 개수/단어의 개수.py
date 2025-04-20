import sys
input = sys.stdin.readline


# 문자열을 공백 단위로 받아서 리스트에 저장
# 단 입력 받을때 strip 적용해서 받고 그 후에 나눠야 함 



if __name__ == "__main__":
    string = input().strip()

    str_list = string.split()
    print(len(str_list))


    