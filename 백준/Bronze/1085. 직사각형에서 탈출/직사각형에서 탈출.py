x,y,w,h = map(int,input().split())

if x < w - x:
    min_width = x
else:
    min_width = w - x

if y < h - y:
    min_length = y
else:
    min_length = h - y

if min_length < min_width:
    print(min_length)
else:
    print(min_width)