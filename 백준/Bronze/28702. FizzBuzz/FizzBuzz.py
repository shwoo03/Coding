import math
import heapq
from collections import deque
from itertools import permutations, combinations
import sys
input = sys.stdin.readline


def check_fizzbuzz(number):
    if number % 15 == 0:  
        print("FizzBuzz")
    elif number % 3 == 0: 
        print("Fizz")
    elif number % 5 == 0: 
        print("Buzz")
    else:                 
        print(number)


if __name__ == "__main__":
    a = input().strip()
    b = input().strip()
    c = input().strip()

    if a.isdigit():
        num_a = int(a) + 3
        check_fizzbuzz(num_a)
    elif b.isdigit():
        num_b = int(b) + 2
        check_fizzbuzz(num_b)
    elif c.isdigit():
        num_c = int(c) + 1
        check_fizzbuzz(num_c)