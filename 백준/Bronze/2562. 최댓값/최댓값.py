import sys
input = sys.stdin.readline








if __name__ == "__main__":
    num_list = []
    for i in range(9):
        num_list.append(int(input()))

    print(max(num_list))
    print(num_list.index(max(num_list)) + 1)