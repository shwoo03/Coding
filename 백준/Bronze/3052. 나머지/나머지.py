import sys
input = sys.stdin.readline


# 42로 나눈 나머지 이므로 중복 결과를 없애고 len을 구하면 된다.



if __name__ == "__main__":
    num_list = []

    for i in range(10):
        num_list.append(int(input()) % 42)
    
    print(len(set(num_list)))

    