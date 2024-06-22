import math as m

d,h_ratio,w_ratio = map(int,input().split())
h = d * h_ratio / m.sqrt(h_ratio * h_ratio + w_ratio * w_ratio)
w = d * w_ratio / m.sqrt(h_ratio * h_ratio + w_ratio * w_ratio)

h = m.floor(h)
w = m.floor(w)
print(h, w)