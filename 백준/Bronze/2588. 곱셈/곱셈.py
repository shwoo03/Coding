import sys
input = sys.stdin.readline








if __name__ == "__main__":
    num1 = input().strip()
    num2 = input().strip()

    for i in range(3):
        print(int(num1) * int(num2[2 - i]))  
    
    print(int(num1) * int(num2))