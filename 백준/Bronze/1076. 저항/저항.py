value = {
    'black' : '0',
    'brown' : '1',
    'red' : '2',
    'orange' : '3',
    'yellow' : '4',
    'green' : '5',
    'blue' : '6',
    'violet' : '7',
    'grey' : '8',
    'white' : '9'
}

mul = {
    'black' : 1,
    'brown' : 10,
    'red' : 100,
    'orange' : 1000,
    'yellow' : 10000,
    'green' : 100000,
    'blue' : 1000000,
    'violet' : 10000000,
    'grey' : 100000000,
    'white' : 1000000000
}

v = 0
ch = input()
ch2 = input()
ch3 = input()
v = int(value[ch]+value[ch2])
print(v * mul[ch3])



