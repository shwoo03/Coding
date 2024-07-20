dict_alpha = {
    'c=' : 1,
    'c-' : 1,
    'dz=' : 1,
    'd-' : 1,
    'lj' : 1,
    'nj' : 1,
    's=' : 1,
    'z=' : 1
}

input_str = input().strip()
total_length = 0
i = 0

while i < len(input_str):
    # 최대 3글자 이므로 3글자로 비교하고 일치하면 3글자를 더해준다.
    if input_str[i:i+3] == 'dz=':
        total_length += 1
        i += 3
    # 2글자로 비교하고 일치하면 2글자를 더해준다.
    elif input_str[i:i+2] in dict_alpha:
        total_length += 1
        i += 2
    # 일치하지 않으면 1글자를 더해준다.
    else:
        total_length += 1
        i += 1

print(total_length)