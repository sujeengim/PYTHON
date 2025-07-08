#11047
import sys

n, k = map(int, input().strip().split())
nlist = []  # 동전 종류
gap = k
cnt = 0

for i in range(n):
    na = int(sys.stdin.readline().strip())
    nlist.append(na)

'''
n: 동전의 종류 수
k: 동전의 총합 목표
nlist[-1] : 처음 목표에 가장 가까운 동전
gap : 현재 목표와 차이
cnt : 사용된 동전 개수 
'''

nlist.sort(reverse=True)  

# gap 줄여가기 
for i in range(len(nlist)):
    while gap > 0:
        if gap - nlist[i] >= 0:
            u = gap//nlist[i]
            gap -= nlist[i] * u
            cnt += u
        else:
            break

print(cnt)
