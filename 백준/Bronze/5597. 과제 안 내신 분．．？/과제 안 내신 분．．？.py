import sys
input = sys.stdin.readline






if __name__ == "__main__":
    list_student = [False] * 30

    for index in range(28):
        input_index = int(input())

        list_student[input_index - 1] = True

    
    print(list_student.index(False) + 1)
    print(list_student.index(False, list_student.index(False) + 1) + 1)
    

