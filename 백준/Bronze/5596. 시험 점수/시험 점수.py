mingook = list(map(int,input().split()))
manse = list(map(int,input().split()))

total_mingook = sum(mingook)
total_manse = sum(manse)

if total_manse == total_mingook:
    print(total_mingook)
elif total_mingook > total_manse:
    print(total_mingook)
else:
    print(total_manse)