a = input()
b = input()
c = input()

def numerical_judgment(a,b,c):
    if(a.isdigit()):
        return int(a) + 3
    elif(b.isdigit()):
        return int(b) + 2
    elif(c.isdigit()):
        return int(c) + 1

num = numerical_judgment(a,b,c)

def fizzbuzz(num):
    if(num % 3 == 0 and num % 5 == 0):
        return "FizzBuzz"
    elif(num % 3 == 0):
        return "Fizz"
    elif(num % 5 == 0):
        return "Buzz"
    else:
        return num

print(fizzbuzz(num))