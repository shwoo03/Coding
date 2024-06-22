def rot13(text):
    rot13_table = str.maketrans(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
        'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    )
    
    return text.translate(rot13_table)

text = input()

enc = rot13(text)
print(enc)