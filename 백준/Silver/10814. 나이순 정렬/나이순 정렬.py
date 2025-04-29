import math
import sys
input = sys.stdin.readline


# 나이, 가입 순서 순으러 정렬하기 


if __name__ == "__main__":
    T = int(input())
    list_member = []

    for i in range(T):
        age, name = input().split()
        list_member.append([int(age), name, i])
    
    ordered_list_member = sorted(list_member, key=lambda member: (member[0], member[2]))

    for member_info in ordered_list_member:
        print(member_info[0], member_info[1])