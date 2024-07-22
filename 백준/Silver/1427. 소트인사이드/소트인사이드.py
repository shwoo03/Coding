input_str = input()
numbers = list(map(int, list(input_str)))

numbers.sort(reverse=True)

for number in numbers:
    print(number, end='')