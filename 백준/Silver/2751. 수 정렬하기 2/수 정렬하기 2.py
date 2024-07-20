import sys
input = sys.stdin.read
output = sys.stdout.write

def main():
    data = input().split()
    N = int(data[0])
    list_num = list(map(int, data[1:]))
    
    list_num.sort()
    
    output('\n'.join(map(str, list_num)) + '\n')

if __name__ == "__main__":
    main()
