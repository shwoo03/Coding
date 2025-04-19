import sys
input = sys.stdin.readline








if __name__ == "__main__":
    string = input().strip()
    word_count = [0] * 26

    for ch in string:
        word_count[ord(ch) - ord('a')] += 1
    
    print(*word_count)
