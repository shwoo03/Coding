# Day Of Mourning의 기타리스트 강토가 사용하는 기타에서 N개의 줄이 끊어졌다. 따라서 새로운 줄을 사거나 교체해야 한다. 
# 강토는 되도록이면 돈을 적게 쓰려고 한다. 6줄 패키지를 살 수도 있고, 1개 또는 그 이상의 줄을 낱개로 살 수도 있다.
# 끊어진 기타줄의 개수 N과 기타줄 브랜드 M개가 주어지고, 각각의 브랜드에서 파는 기타줄 6개가 들어있는 패키지의 가격, 
# 낱개로 살 때의 가격이 주어질 때, 적어도 N개를 사기 위해 필요한 돈의 수를 최소로 하는 프로그램을 작성하시오.

N, M = map(int, input().split())

package = []
single = []

for i in range(M):
    a, b = map(int, input().split())
    package.append(a)
    single.append(b)

package.sort()
single.sort()

total_only_package = (N // 6) * package[0] + (package[0] if N % 6 > 0 else 0)
total_package_single = (N // 6) * package[0] + (N % 6) * single[0] 
total_only_single = N * single[0]

print(min(total_only_package, total_package_single, total_only_single))