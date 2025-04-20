import sys
input = sys.stdin.readline





if __name__ == "__main__":
    list_alpha = [-1] * 26
    S = input().strip()

    for index, ch in enumerate(S):
        idx = ord(ch) - ord('a')
        if list_alpha[idx] == -1:
            list_alpha[idx] = index

    print(*list_alpha)
