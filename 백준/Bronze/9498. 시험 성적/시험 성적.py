import sys
input = sys.stdin.readline








if __name__ == "__main__":
    score = int(input())

    if(score > 89):
        print("A")
    elif(score > 79):
        print("B")
    elif(score > 69):
        print("C")
    elif(score > 59):
        print("D")
    else:
        print("F")
