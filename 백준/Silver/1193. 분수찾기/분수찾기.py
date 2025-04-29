import math
import sys
input = sys.stdin.readline




if __name__ == "__main__":
    X = int(input())

    line = 1
    while X > (line * (line + 1)) // 2:
        line += 1

    start_num = (line * (line - 1)) // 2 + 1
    pos_in_line = X - start_num + 1

    if line % 2 == 0:
        numerator = pos_in_line
        denominator = line - pos_in_line + 1
    else:
        numerator = line - pos_in_line + 1
        denominator = pos_in_line

    print(f"{numerator}/{denominator}")
