n = int(input()) # 통화 개수 
list_time = list(map(int,input().split()))
m_total = 0
y_total = 0

for i in list_time:
    y_total += ((i // 30) + 1) * 10
    m_total += ((i // 60) + 1) * 15

if m_total > y_total:
    print(f"Y {y_total}")
elif m_total < y_total:
    print(f"M {m_total}")
elif m_total == y_total:
    print(f"Y M {y_total}")