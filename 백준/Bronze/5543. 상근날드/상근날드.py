hamberger1 = int(input())
hamberger2 = int(input())
hamberger3 = int(input())

drink1 = int(input())
drink2 = int(input())

min_hamberger = min(hamberger1, hamberger2, hamberger3)
min_drink = min(drink1, drink2)

print(min_hamberger + min_drink - 50)