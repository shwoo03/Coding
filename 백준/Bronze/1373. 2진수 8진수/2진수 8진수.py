def split_str(text, size=3, padding='0'):
    padding_needed = (size - len(text) % size) % size
    text = padding * padding_needed + text
    
    
    result = [text[i:i+size] for i in range(0, len(text), size)]
    return result

def conversion(binary_str):
    list_digit = split_str(binary_str)
    result_str = ''
    
    for digit in list_digit:
        octal_digit = str(int(digit, 2))  
        result_str += octal_digit
        
    return result_str

binary_str = input()
result = conversion(binary_str)
print(result)
