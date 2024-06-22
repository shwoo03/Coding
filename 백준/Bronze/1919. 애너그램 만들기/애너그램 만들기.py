a = list(input())
b = list(input())

a_copy = a[:]
b_copy = b[:]

result_a = [x for x in a if not x in b_copy or b_copy.remove(x)]
result_b = [x for x in b if not x in a_copy or a_copy.remove(x)]

print(len(result_a) + len(result_b))