import sys
input = sys.stdin.readline





if __name__ == "__main__":
    num = 1

    for i in range(3):
        num *= int(input())
    
    num_list = list(str(num))
    result = [0] * 10
    for n in num_list:
        result[int(n)] += 1

    for count in result:
        print(count)

