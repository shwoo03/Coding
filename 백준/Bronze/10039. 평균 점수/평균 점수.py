import sys
input = sys.stdin.readline








if __name__ == "__main__":
    scores = []

    for i in range(5):
        x = int(input())
        scores.append(40 if x < 40 else x)
    
    print(sum(scores) // 5)

